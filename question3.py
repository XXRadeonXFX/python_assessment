"""
Q3. In DevOps, automating configuration management tasks is essential for maintaining consistency and managing infrastructure efficiently.

?       The program should read a configuration file (you can provide them with a sample configuration file)
?       It should extract specific key-value pairs from the configuration file.
?       The program should store the extracted information in a data structure (e.g., dictionary or list).
?       It should handle errors gracefully in case the configuration file is not found or cannot be read.
?       Finally save the output file data as JSON data in the database.
?       Create a GET request to fetch this information.
Sample Configuration file: 
[Database]
host = localhost
port = 3306
username = admin
password = secret

[Server]
address = 192.168.0.1
port = 8080

Sample Output: 
Configuration File Parser Results:
Database:
- host: localhost
- port: 3306
- username: admin
- password: secret

Server:
- address: 192.168.0.1
- port: 8080 
"""


import configparser
import json
from flask import Flask, jsonify

app = Flask(__name__)

def parse_config(file_path):
    config = configparser.ConfigParser()
    try:
        config.read(file_path)
        config_data = {section: dict(config.items(section)) for section in config.sections()}
        return config_data
    except FileNotFoundError:
        print("Error: Configuration file not found.")
        return {}
    except Exception as e:
        print(f"Error: {e}")
        return {}

@app.route("/get-config", methods=["GET"])
def get_config():
    config_data = parse_config("sample_config.ini")
    if config_data:
        with open("config_output.json", "w") as f:
            json.dump(config_data, f, indent=4)
        return jsonify(config_data)
    else:
        return jsonify({"error": "Failed to parse configuration file."}), 500

if __name__ == "__main__":
    app.run(port=5000)
