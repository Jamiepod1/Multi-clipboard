import sys
import json
import clipboard

JSON_FILE = "clipboard_data.json"


def paste(filepath, data):
    with open(filepath, "w") as f:
        json.dump(data, f)


def copy(filepath):
    try:
        with open(filepath, "r") as f:
            data = json.load(f)
            return data
    except FileNotFoundError:
        return {}


if len(sys.argv) == 2:
    command = sys.argv[1]
    data = copy(JSON_FILE)

    if command == "copy":
        key = input("What do you want to copy to clipboard? ")

        if key in data:
            clipboard.copy(data[key])
            print("Copied to clipboard:", data[key])

        else:
            print("Clipboard item does not exist")

    elif command == "paste":
        key = input("What do you want to paste to multi-clipboard? ")
        data[key] = clipboard.paste()
        paste(JSON_FILE, data)
        print("Pasted to multi-clipboard:")
        print(f"{key}: {data[key]}")
    elif command == "list":
        data = copy(JSON_FILE)
        for key in data:
            print(f"{key}: {data[key]}")
    else:
        print("Unknown command, please use:")
        print("copy")
        print("paste")
        print("list")
else:
    print("Please pass one command:")
    print("copy")
    print("paste")
    print("list")
