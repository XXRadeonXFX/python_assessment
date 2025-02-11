"""
Q3. In DevOps, automating configuration management tasks is essential for maintaining consistency and managing infrastructure efficiently.

(*) The program should read a configuration file (you can provide them with a sample configuration file)
(*) It should extract specific key-value pairs from the configuration file.
(*) The program should store the extracted information in a data structure (e.g., dictionary or list).
(*) It should handle errors gracefully in case the configuration file is not found or cannot be read.
(*) Finally save the output file data as JSON data in the database.
(*) Create a GET request to fetch this information.

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
import pymongo
import os
from flask import Flask, jsonify

# Initialize Flask app
app = Flask(__name__)

# Configuration file path
CONFIG_FILE = os.path.join(os.path.dirname(__file__), "config.ini")
MONGO_URI = "mongodb://localhost:27017"
DATABASE_NAME = "configDB"
COLLECTION_NAME = "configData"

def parse_config(file_path):
    """Parses a configuration file and extracts key-value pairs."""
    config = configparser.ConfigParser()
    
    # Check if file exists
    if not os.path.exists(file_path):
        print(f"ERROR: Config file '{file_path}' not found!")
        return None
    
    try:
        print(f"Reading config file: {file_path}")
        config.read(file_path, encoding="utf-8")
        
        if not config.sections():
            print(f"ERROR: No sections found in '{file_path}'. Check file format!")
            return None
        
        print(f"Sections found: {config.sections()}")
        config_dict = {section: dict(config.items(section)) for section in config.sections()}
        return config_dict
    except Exception as e:
        print(f"Error reading config file: {e}")
        return None

def save_to_mongo(data):
    """Saves JSON data to MongoDB."""
    try:
        client = pymongo.MongoClient(MONGO_URI)
        db = client[DATABASE_NAME]
        collection = db[COLLECTION_NAME]
        
        # Insert JSON data into MongoDB
        print("Saving to MongoDB:", json.dumps(data, indent=4))
        collection.insert_one(data)
        
        print("Data saved to MongoDB successfully.")
    except Exception as e:
        print(f"Error saving to MongoDB: {e}")

@app.route('/get_config', methods=['GET'])
def get_config():
    """API Endpoint to fetch stored configuration."""
    try:
        client = pymongo.MongoClient(MONGO_URI)
        db = client[DATABASE_NAME]
        collection = db[COLLECTION_NAME]
        result = collection.find_one(sort=[("_id", -1)])
        
        if result:
            del result["_id"]  # Remove MongoDB object ID for cleaner output
            return jsonify(result)
        else:
            return jsonify({"message": "No configuration data found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    # Print working directory for debugging
    print("Current Working Directory:", os.getcwd())
    
    # Parse configuration file
    config_data = parse_config(CONFIG_FILE)
    
    if config_data:
        print("Configuration File Parsed Successfully:")
        print(json.dumps(config_data, indent=4))
        
        # Save to MongoDB
        save_to_mongo(config_data)
    else:
        print("Failed to parse configuration file. Ensure the file exists and is correctly formatted.")
    
    # Start Flask API
    app.run(debug=True, port=5000)

