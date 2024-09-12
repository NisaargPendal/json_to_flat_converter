# JSON to Flat Converter

![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![Flask](https://img.shields.io/badge/Flask-2.0%2B-green)

A Flask web application that converts nested JSON structures into a flat key-value format.

## 📋 Table of Contents
- [Features](#-features)
- [Installation](#-installation)
- [Usage](#-usage)
- [Troubleshooting](#-troubleshooting)
- [Code Explanation](#-code-explanation)
- [Contributing](#-contributing)
- [License](#-license)

## ✨ Features

- Convert nested JSON to flat key-value pairs
- Web interface for easy input and output
- Error handling for invalid JSON input
- Debug information for troubleshooting

## 🚀 Installation

1. **Clone the repository:**
   git clone https://github.com/yourusername/json-to-flat-converter.git
   
   **Change the directory to :**
    ```
    cd json-to-flat-converter
    ```
2. **Create a virtual environment:**
    ```
    python3 -m venv venv
    ```
3. **Activate the virtual environment:**
   - On Unix or MacOS:
    ```     
    source venv/bin/activate
    ```   
   - On Windows:
   ```
    venv\Scripts\activate
   ```
4. **Install required packages:**
     ```
    pip install flask
    ```
5. **Run Script :**
   ```
   python3 app.py
   ```
## 🖥️ Usage

1. **Run the Flask application:**
   python app.py

2. **Open a web browser** and navigate to `http://localhost:5000`

3. **Enter your JSON data** in the provided text area and click "Convert"

4. The **flattened output** will be displayed below the input form

## 🔧 Troubleshooting

### ImportError: cannot import name 'url_quote' from 'werkzeug.urls'

This error occurs due to a version mismatch between Flask and Werkzeug. To resolve:

1. **Upgrade Flask and Werkzeug:**
   pip install --upgrade flask werkzeug

2. If the error persists, **try installing specific versions:**
   pip uninstall flask werkzeug
   pip install flask==2.0.3 werkzeug==2.0.3

3. If issues continue, **create a new virtual environment:**
   deactivate
   python3 -m venv new_venv
   source new_venv/bin/activate
   pip install flask

4. As a last resort, **modify the Flask code:**
   - Open `venv/lib/python3.12/site-packages/flask/helpers.py`
   - Change `from werkzeug.urls import url_quote` to `from werkzeug.urls import quote as url_quote`

### Other Troubleshooting Steps

- **Check Flask and Werkzeug versions:**
  pip freeze | grep -E "Flask|Werkzeug"
- **Verify Python version:**
  python --version
- **Ensure the `templates` folder exists** and contains `index.html`

## 📝 Code Explanation

The main components of the application are:

1. `json_to_flat_converter()`: Converts nested JSON to flat key-value pairs
2. Flask route `/`: Handles both GET and POST requests
3. Error handling for JSON parsing and template rendering
4. Debug information gathering for troubleshooting

Key points in the code:

- Uses type hints for better code readability
- Implements error handling for invalid JSON input
- Includes debug information for easier troubleshooting

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

---

<details>
<summary>📌 Note for Developers</summary>

When contributing to this project, please ensure that you:

- Follow the existing code style
- Write unit tests for new features
- Update the README if you make significant changes

Thank you for your contributions!
</details>
