"""
Q4. In DevOps, performing regular backups of important files is crucial:

(*) Implement a Python script called backup.py that takes a source directory and a destination directory as command-line arguments.
(*) The script should copy all files from the source directory to the destination directory.
(*) Before copying, check if the destination directory already contains a file with the same name. If so, append a timestamp to the file name to ensure uniqueness.
(*) Handle errors gracefully, such as when the source directory or destination directory does not exist.

Sample Command:
python backup.py /path/to/source /path/to/destination
By running the script with the appropriate source and destination directories, it should create backups of the files in the source directory, ensuring unique file names in the destination directory.
"""

import os
import shutil
import sys
from datetime import datetime

def backup_files(source_dir, dest_dir):
    try:
        if not os.path.exists(source_dir):
            raise FileNotFoundError(f"Source directory '{source_dir}' does not exist.")
        if not os.path.exists(dest_dir):
            os.makedirs(dest_dir)
        
        for file_name in os.listdir(source_dir):
            source_file = os.path.join(source_dir, file_name)
            if os.path.isfile(source_file):
                dest_file = os.path.join(dest_dir, file_name)
                if os.path.exists(dest_file):
                    base, ext = os.path.splitext(file_name)
                    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
                    dest_file = os.path.join(dest_dir, f"{base}_{timestamp}{ext}")
                shutil.copy2(source_file, dest_file)
                print(f"Copied: {source_file} -> {dest_file}")
        print("Backup completed successfully.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python backup.py <source_dir> <dest_dir>")
    else:
        source_dir = sys.argv[1]
        dest_dir = sys.argv[2]
        backup_files(source_dir, dest_dir)
