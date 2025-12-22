from flask import Flask, render_template, request, redirect, url_for
import qrcode
import os
import json
import time

app = Flask(__name__)

# Folder to save QR images
QR_FOLDER = "static/qrcodes"
os.makedirs(QR_FOLDER, exist_ok=True)

# JSON file to store QR data
DATA_FILE = "qr-data.json"

# Load QR data
def load_data():
    try:
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    except:
        return {}

# Save QR data
def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f)

# Home page: generate QR
@app.route("/", methods=["GET", "POST"])
def index():
    data = load_data()
    qr_url = None
    qr_id = None

    if request.method == "POST":
        text = request.form.get("qrText")
        if text:
            # Create a unique ID for this QR
            qr_id = int(time.time())  # simple unique ID using timestamp
            qr_filename = f"qr_{qr_id}.png"
            qr_path = os.path.join(QR_FOLDER, qr_filename)

            # Generate QR code
            img = qrcode.make(f"{request.host_url}scan/{qr_id}")
            img.save(qr_path)

            # Save data in JSON
            data[str(qr_id)] = {"text": text, "filename": qr_filename, "count": 0}
            save_data(data)

            qr_url = url_for("static", filename=f"qrcodes/{qr_filename}")

    return render_template("index.html", qr_url=qr_url, qr_id=qr_id, data=data)

# Scan route: increase count and redirect
@app.route("/scan/<int:qr_id>")
def scan(qr_id):
    data = load_data()
    str_id = str(qr_id)

    if str_id in data:
        data[str_id]["count"] += 1
        save_data(data)
        return redirect(data[str_id]["text"])

    return "QR not found", 404

# Run app
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)