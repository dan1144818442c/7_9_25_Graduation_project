import os
from pathlib import Path
from datetime import datetime

class Loader:

    @staticmethod
    def get_file_paths_in_list(directory_path):
        file_paths = []
        for filename in os.listdir(directory_path):
            full_path = os.path.join(directory_path, filename)
            if os.path.isfile(full_path):  # Check if it's a file, not a subdirectory
                file_paths.append(full_path)
        return file_paths

    @staticmethod
    def get_metadata_of_file(file_path):
        orginal_file_path = file_path
        file_path = Path(file_path)
        if file_path.exists():
            stats = file_path.stat()
            last_modidied = datetime.fromtimestamp(stats.st_mtime).strftime("%Y-%m-%d %H:%M:%S")
            creation_timestamp = datetime.fromtimestamp(stats.st_ctime).strftime("%Y-%m-%d %H:%M:%S")

            dic_data = {'Name': str(file_path.name),
                        'Stem': file_path.stem,
                        "Suffix": file_path.suffix,
                        "Parent": str(file_path.parent),
                        "File size": stats.st_size,
                        "Last modified": str(last_modidied),
                        'creation_datetime':str(creation_timestamp),
                        'file path with type': str(file_path) ,
                        'file path' : str(orginal_file_path)
                        }
            return dic_data
        print(str(file_path)  + " not found")
        return "file not found"

