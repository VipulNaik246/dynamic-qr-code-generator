# Dynamic QR Code Generator

A simple Flask-based web application that generates QR codes from text or URLs and tracks how many times each QR code is scanned.

This project is useful for creating shareable links, tracking user engagement, and generating scan-based analytics in a lightweight way.

## Overview

The application allows users to:

- Enter any text or URL
- Generate a QR code instantly
- Save the QR image in the project folder
- Track scan count for each QR code
- Redirect scanned QR users to the original link

## Features

- Generate QR codes from text or URLs
- Store QR metadata in a JSON file
- Count how many times each QR code is scanned
- Redirect to the original destination when scanned
- Lightweight Flask app with minimal setup
- Easy to run locally for testing or demos

## Tech Stack

- Python
- Flask
- qrcode
- JSON for storing metadata
- HTML / CSS / JavaScript

## Project Structure

```text
dynamic-qr-generator/
├── app.py                 # Main Flask application
├── qr-data.json           # Stores QR metadata and scan counts
├── qrdata.db              # Database file if used in local setup
├── requirements.txt       # Python dependencies
├── runtime.txt            # Runtime configuration
├── static/
│   └── qrcodes/           # Generated QR images
├── templates/
│   └── index.html         # Frontend page
├── README.md              # Project documentation
└── .gitignore             # Ignore local/system files
```

## Prerequisites

Before running the project, make sure you have:

- Python 3.9+
- pip installed
- A terminal or command prompt

## Installation

1. Clone the repository
2. Open the project folder
3. Create and activate a virtual environment:

```bash
python -m venv .venv
```

On Windows:

```powershell
.venv\Scripts\Activate.ps1
```

On macOS/Linux:

```bash
source .venv/bin/activate
```

4. Install the dependencies:

```bash
pip install -r requirements.txt
```

## Run the Application

Start the app using:

```bash
python app.py
```

Then open the browser at:

```text
http://127.0.0.1:5000/
```

## How It Works

1. Enter a URL or text in the web form
2. The app creates a QR code image
3. The QR points to a scan route
4. Each time the QR is scanned, the count increases
5. The original destination is opened after scan

## Example Usage

Type a URL like:

```text
https://example.com
```

and the app will generate a QR image linked to that URL.

## Security Notes

- Do not expose private URLs or sensitive links in public demo projects.
- Keep generated QR files and data safe in local environments.
- Use environment variables or secure config values for production deployment.

## GitHub Repository

This project is connected to GitHub here:

```text
https://github.com/VipulNaik246/dynamic-qr-code-generator.git
```

## License

This project is intended for learning and demonstration purposes.

## Contributing

Contributions are welcome. You can improve the frontend, add a dashboard, or extend scan analytics for a more production-ready QR system.

## Contact

For questions or improvements, contact the project maintainer or repository owner.
