from flask import Flask, render_template, request, redirect, url_for, jsonify
import qrcode
import os
import json
import uuid

app = Flask(__name__)

# Folder to save QR images
QR_FOLDER = "static/qrcodes"
os.makedirs(QR_FOLDER, exist_ok=True)

# JSON file to store QR data
DATA_FILE = "qr-data.json"

# 🔥 PUT YOUR ACTUAL IPv4 ADDRESS HERE
LAPTOP_IP = "172.18.203.24"

# -----------------------------
# Load QR data
# -----------------------------
def load_data():
    if not os.path.exists(DATA_FILE):
        return {}
    with open(DATA_FILE, "r") as f:
        return json.load(f)

# -----------------------------
# Save QR data
# -----------------------------
def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

# -----------------------------
# Home Page (Generate QR)
# -----------------------------
@app.route("/", methods=["GET", "POST"])
def index():
    qr_image = None
    qr_id = None
    count = None

    if request.method == "POST":
        text = request.form.get("text")  # must match HTML input name

        if text:
            data = load_data()

            # Unique ID
            qr_id = str(uuid.uuid4())

            qr_filename = f"qr_{qr_id}.png"
            qr_path = os.path.join(QR_FOLDER, qr_filename)

            # This is the link inside QR
            qr_link = f"http://{LAPTOP_IP}:5000/scan/{qr_id}"

            # Generate QR
            img = qrcode.make(qr_link)
            img.save(qr_path)

            # Save data
            data[qr_id] = {
                "text": text,
                "filename": qr_filename,
                "count": 0
            }
            save_data(data)

            qr_image = url_for("static", filename=f"qrcodes/{qr_filename}")
            count = 0

    return render_template(
        "index.html",
        qr_image=qr_image,
        qr_id=qr_id,
        count=count
    )

# -----------------------------
# Scan Route (Increase Count)
# -----------------------------
@app.route("/scan/<qr_id>")
def scan(qr_id):
    data = load_data()

    if qr_id in data:
        data[qr_id]["count"] += 1
        save_data(data)

        return redirect(data[qr_id]["text"])

    return "QR not found", 404

# -----------------------------
# API Route for Live Count
# -----------------------------
@app.route("/count/<qr_id>")
def get_count(qr_id):
    data = load_data()

    if qr_id in data:
        return jsonify({"count": data[qr_id]["count"]})

    return jsonify({"count": 0})

# -----------------------------
# Run App
# -----------------------------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
