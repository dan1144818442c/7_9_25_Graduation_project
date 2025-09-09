import os
from pathlib import Path
from datetime import datetime
from logger_ import log
class Loader:

    @staticmethod
    def get_file_paths_in_list(directory_path):
        logger  = log.Logger.get_logger()
        file_paths = []
        try :
            for filename in os.listdir(directory_path):
                full_path = os.path.join(directory_path, filename)
                if os.path.isfile(full_path):  # Check if it's a file, not a subdirectory
                    file_paths.append(full_path)
            logger.info("All file paths were successfully collected.")

            return file_paths

        except Exception as e:
            logger.error(f"Faild get all All file paths from {directory_path} - {e}")

    @staticmethod
    def get_metadata_of_file(file_path):
        logger = log.Logger.get_logger()
        orginal_file_path = file_path
        try :
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
                logger.info("The dictionary is created with all the META DATA.")
                return dic_data
        except Exception as e:
            logger.error(f"faild created the dictionary with all the META DATA.  - {e}")
            

