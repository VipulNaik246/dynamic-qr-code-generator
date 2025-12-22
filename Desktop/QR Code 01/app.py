from flask import Flask, render_template, request, redirect, jsonify
import qrcode
import os
import json
import socket

app = Flask(__name__)

QR_FOLDER = "static/qrcodes"
os.makedirs(QR_FOLDER, exist_ok=True)

# JSON file to store QR info
DATA_FILE = "qr_data.json"

# Load existing data
if os.path.exists(DATA_FILE):
    with open(DATA_FILE, "r") as f:
        qr_data = json.load(f)
        qr_data = {int(k): v for k, v in qr_data.items()}  # keys as int
else:
    qr_data = {}

# Find next QR id
qr_id = max(qr_data.keys(), default=0)

# Get local IP automatically
def get_local_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # doesn't need to be reachable
        s.connect(("10.255.255.255", 1))
        IP = s.getsockname()[0]
    except:
        IP = "127.0.0.1"
    finally:
        s.close()
    return IP

LOCAL_IP = get_local_ip()


# Save QR data to JSON
def save_data():
    with open(DATA_FILE, "w") as f:
        json.dump(qr_data, f)


@app.route("/")
def index():
    return render_template("index.html", qr_image=None, count=None)


@app.route("/generate", methods=["POST"])
def generate():
    global qr_id
    text = request.form["text"]
    qr_id += 1

    scan_url = f"http://{LOCAL_IP}:5000/scan/{qr_id}"

    # Generate QR
    img = qrcode.make(scan_url)
    filename = f"{qr_id}.png"
    img.save(os.path.join(QR_FOLDER, filename))

    # Save QR info
    qr_data[qr_id] = {"target": text, "count": 0}
    save_data()

    return render_template(
        "index.html",
        qr_image=f"/static/qrcodes/{filename}",
        count=0,
        qr_id=qr_id
    )


@app.route("/scan/<int:id>")
def scan(id):
    if id in qr_data:
        qr_data[id]["count"] += 1
        save_data()
        return redirect(qr_data[id]["target"])
    return "Invalid QR"


# API to get scan count (for live update)
@app.route("/count/<int:id>")
def get_count(id):
    if id in qr_data:
        return jsonify({"count": qr_data[id]["count"]})
    return jsonify({"count": 0})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)