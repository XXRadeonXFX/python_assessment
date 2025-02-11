# 📌 Python Assessment

## 📖 Overview

This repository contains a collection of Python assessment scripts designed to solve various problems. These scripts demonstrate proficiency in Python programming, including working with configuration files, databases, APIs, and automation.

## 📂 Repository Structure

The repository includes the following files:

- **`question1.py`** - Solution to the first assessment task.
- **`question2.py`** - Solution to the second assessment task.
- **`question3.py`** - Solution to the third assessment task (parsing configuration files and storing them in MongoDB).
- **`question4.py`** - Solution to the fourth assessment task.
- **`config.ini`** - Sample configuration file used by `question3.py`.
- **`README.md`** - This file, providing an overview of the repository.

## 🚀 Getting Started

### ✅ Prerequisites

To run the scripts, ensure you have the following installed:

- **Python 3.x** ([Download Python](https://www.python.org/downloads/))
- **MongoDB** (for `question3.py`) ([Download MongoDB](https://www.mongodb.com/try/download/community))

### 🔧 Installation

#### 📥 Clone the Repository
```sh
git clone https://github.com/XXRadeonXFX/python_assessment.git
cd python_assessment
```

#### 🏗️ Create and Activate a Virtual Environment (Recommended)
```sh
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

#### 📦 Install Required Dependencies
```sh
pip install -r requirements.txt
```
> **Note:** If `requirements.txt` is not available, install dependencies manually as needed.

## 🏃 Running the Scripts

Each script can be executed individually. Follow the specific instructions below:

### ▶️ Running `question1.py`
```sh
python question1.py
```

### ▶️ Running `question2.py`
```sh
python question2.py
```

### ▶️ Running `question3.py` (Configuration File Parser with MongoDB)
#### 🛠 Ensure MongoDB is running:
```sh
mongod --dbpath /path/to/data/db  # Modify path accordingly
```

#### 🚀 Run the script:
```sh
python question3.py
```

#### 🗄 Verify data in MongoDB:
```sh
mongo
use configDB
db.configData.find().pretty()
```

### ▶️ Running `question4.py`
```sh
python question4.py
```

## 🌐 API Endpoints

`question3.py` includes a **Flask API** to retrieve stored configuration data from MongoDB.

### 🌟 Start the API
```sh
python question3.py
```

### 📡 Access Configuration Data
Open your browser or use Postman to visit:
```sh
http://127.0.0.1:5000/get_config
```

## ⚙️ Configuration File (`config.ini`)
The `config.ini` file contains the following structure:

```ini
[Database]
host = localhost
port = 3306
username = admin
password = secret

[Server]
address = 192.168.0.1
port = 8080
```

Ensure this file is correctly formatted and present in the repository root before running `question3.py`.

## 🛠 Troubleshooting

### ❌ MongoDB Connection Issues
- Ensure MongoDB is running.
- Check the connection string in `question3.py`.

### ❌ Configuration File Not Found
- Ensure `config.ini` is in the correct location.
- Verify file permissions.

### ❌ Flask API Not Working
- Check for port conflicts.
- Ensure Flask is installed (`pip install flask`).

---

✨ *Feel free to modify and expand upon this project as needed!* 🚀

