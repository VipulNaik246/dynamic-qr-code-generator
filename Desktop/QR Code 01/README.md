# QR Code Generator with Scan Count

This is a full-stack QR Code Generator project built using Python Flask and HTML/CSS.

## Features
- Generate QR code from text or URL
- Each QR code is unique
- Scan count increases every time QR is scanned
- Scan data is stored persistently
- Simple and clean UI

## Tech Stack
- Python
- Flask
- HTML
- CSS
- qrcode library

## Project Structure
QR Code 01/
├── app.py
├── qr_data.json
├── templates/
│   └── index.html
├── static/
│   ├── style.css
│   └── qrcodes/
└── README.md

## How to Run the Project
1. Install dependencies:
   pip install flask qrcode pillow

2. Run the app:
   python app.py

3. Open browser:
   http://127.0.0.1:5000

## How Scan Count Works
- QR code points to backend route
- Every scan hits the server
- Server increases scan count
- Count is stored in qr_data.json

## Author
Vipul Naik