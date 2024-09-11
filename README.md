# JSON Flattener

A web application that flattens nested JSON structures. Built with Flask and JavaScript.

## Project Structure

json-flattener/
- app.py
- requirements.txt
- templates/
  - index.html


## Setup

### Linux Setup

First, check your Linux distribution and install the necessary components.

1. Check your Linux distribution:
   ```bash
   cat /etc/os-release
   ```

2. Based on your distribution, follow the appropriate instructions:

   Ubuntu/Debian:
   ```bash
   sudo apt update
   sudo apt install python3 python3-venv python3-pip
   ```

   Arch Linux:
   ```bash
   sudo pacman -Syu
   sudo pacman -S python python-pip
   ```

   Fedora:
   ```bash
   sudo dnf update
   sudo dnf install python3 python3-pip
   ```

   CentOS/RHEL:
   ```bash
   sudo yum update
   sudo yum install python3 python3-pip
   ```

### Project Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/NisaargPendal/json_to_flat_converter.git
   
   cd json-flattener
   ```

2. Create a virtual environment:
   ```bash
   python3 -m venv venv
   ```

3. Activate the virtual environment:
   ```bash
   source venv/bin/activate
   ```

4. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

1. Ensure you're in the project directory and your virtual environment is activated.

2. Run the Flask application:
   ```
   python3 app.py
   ```

3. Open a web browser and navigate to `http://127.0.0.1:5000/`.

## Usage

1. Enter your nested JSON in the "Input JSON" textarea.
2. Click the "Flatten JSON" button.
3. The flattened JSON will appear in the "Flattened Output" section.
4. Use the "Copy" button to copy the flattened JSON to your clipboard.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Contact

Created by Nisarg Pendal - feel free to contact me at nisargpendal@gmail.com!
