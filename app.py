from flask import Flask, render_template, request
import json
from typing import Any, Dict
import os

app = Flask(__name__)

def json_to_flat_converter(data: Any, prefix: str = '') -> Dict[str, Any]:
    result: Dict[str, Any] = {}
    if isinstance(data, dict):
        for key, value in data.items():
            result.update(json_to_flat_converter(value, f"{prefix}{key}."))
    elif isinstance(data, list):
        for i, item in enumerate(data):
            result.update(json_to_flat_converter(item, f"{prefix}{i}."))
    else:
        result[prefix.rstrip('.')] = data
    return result

@app.route('/', methods=['GET', 'POST'])
def index():
    flattened_output = ""
    error_message = ""
    debug_info = f"Current working directory: {os.getcwd()}\n"
    debug_info += f"Template folder: {app.template_folder}\n"
    debug_info += f"Template folder exists: {os.path.exists(app.template_folder)}\n"
    if os.path.exists(app.template_folder):
        debug_info += f"Files in template folder: {os.listdir(app.template_folder)}\n"
    debug_info += f"index.html exists: {os.path.exists(os.path.join(app.template_folder, 'index.html'))}\n"
    debug_info += f"Full path to index.html: {os.path.join(app.template_folder, 'index.html')}\n"
    
    if request.method == 'POST':
        json_input = request.form['json_input']
        try:
            data = json.loads(json_input)
            flattened = json_to_flat_converter(data)
            flattened_output = "\n".join(f"{key} = {json.dumps(value)}" for key, value in sorted(flattened.items()))
        except json.JSONDecodeError as e:
            error_message = f"Invalid JSON input. Error: {e}"
        except Exception as e:
            error_message = f"An unexpected error occurred: {e}"
    
    try:
        return render_template('index.html', flattened_output=flattened_output, error_message=error_message, debug_info=debug_info)
    except Exception as e:
        return f"Error rendering template: {str(e)}<br><br>Debug Info:<br><pre>{debug_info}</pre>"

if __name__ == '__main__':
    app.run(debug=True)
