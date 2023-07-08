import configparser
import json


# Define Vars
INPUT_FILE = r"C:\Users\test.cmpreset"  # content manager file
OUTPUT_FILE = r"C:\Users\audio.ini"  # AC File
KEY_NAME = "AudioData"  # Specify the key name for the desired config data


# Video Test
#INPUT_FILE = r"C:\Users\test.cmpreset"  # content manager file
#OUTPUT_FILE = r"C:\Users\audio.ini"  # AC File
#KEY_NAME = "VideoData"  # Specify the key name for the desired config data


def convert_file(file1, file2, key):
    # Read the contents of File 1
    with open(file1, 'r') as f:
        file1_contents = f.read()

    # Parse the JSON contents
    json_data = json.loads(file1_contents)

    # Extract the specified key data
    config_data = json_data.get(key, '')

    # Create a new configparser object
    config = configparser.ConfigParser(delimiters='=', allow_no_value=True)

    # Load the config data as an INI file
    config.read_string(config_data)

    # Convert keys to uppercase while writing to output file
    with open(file2, 'w') as f:
        for section in config.sections():
            f.write(f"[{section.upper()}]\n")
            for key in config[section]:
                f.write(f"{key.upper()}={config[section][key]}\n")
            f.write("\n")



# Convert File 1 to match the format of File 2
convert_file(INPUT_FILE, OUTPUT_FILE, KEY_NAME)
