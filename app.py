import json
import sys

def json_to_flat_converter(data, prefix=''):
    result = {}
    if isinstance(data, dict):
        for key, value in data.items():
            result.update(json_to_flat_converter(value, f"{prefix}{key}."))
    elif isinstance(data, list):
        for item in data:
            if isinstance(item, (dict, list)):
                result.update(json_to_flat_converter(item, f"{prefix}"))
            else:
                result[f"{prefix[:-1]}"] = item
    else:
        result[prefix[:-1]] = data
    return result

def main():
    print("Please paste your JSON input (press Ctrl+D on Unix/Linux or Ctrl+Z followed by Enter on Windows to finish):")
    json_input = ""
    try:
        while True:
            try:
                line = input()
                json_input += line + "\n"
            except KeyboardInterrupt:
                break
    except EOFError:
        pass

    json_input = json_input.strip()
    if not json_input:
        print("No input provided. Exiting.")
        return

    try:
        data = json.loads(json_input)
        flattened = json_to_flat_converter(data)
        for key, value in sorted(flattened.items()):
            print(f"{key} = {json.dumps(value)}")
        sys.stdout.flush()  # Flush the output buffer
    except json.JSONDecodeError as e:
        print(f"Invalid JSON input. Error: {e}")
        print("Please make sure your input is valid JSON.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
