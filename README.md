# JSON to Flat Converter

## Introduction
The JSON to Flat Converter is a Python script designed to flatten a hierarchical JSON structure into a flat, key-value format. This can be useful when working with complex JSON data and needing to access the values more easily.

## Installation
To use the JSON to Flat Converter, you need to have Python installed on your system. You can download Python from the [official website](https://www.python.org/downloads/). Once you have Python installed, you can download or clone the repository containing the script.

## Usage
1. Open a text editor and paste your JSON input.
2. Press Ctrl+D on Unix/Linux or Ctrl+Z followed by Enter on Windows to finish inputting the JSON data.
3. The script will process the JSON input and output the flattened key-value pairs.

##output
```
auditing.enabled = true
auditing.file_name = "audit-{Date}.txt"
auditing.path = null
cors.rules.allow = true
cors.rules.origin = "https://contoso.com"
files.locations.alias = "inetpub"
files.locations.claims = "read"
files.locations.path = "%systemdrive%\\inetpub"
host_id = ""
host_name = "My instance of the IIS Administration API"
logging.enabled = true
logging.file_name = "log-{Date}.txt"
logging.min_level = "Error"
logging.path = null
security.access_policy.api.access_key = true
security.access_policy.api.users = "administrators"
security.access_policy.api_keys.access_key = false
security.access_policy.api_keys.users = "administrators"
security.access_policy.system.access_key = true
security.access_policy.system.users = "owners"
security.require_windows_authentication = true
```
## Contributing
If you find any issues or have suggestions for improvements, feel free to open an issue or submit a pull request on the GitHub repository.
