from pathlib import Path
from datetime import datetime, time# file_path = Path("podcasts\download (7).wav")
import config
# # Accessing attributes
# print(f"Name: {file_path.name}")
# print(f"Stem: {file_path.stem}")
# print(f"Suffix: {file_path.suffix}")
# print(f"Parent: {file_path.parent}")
#
# # Checking existence and type
# print(f"Exists: {file_path.exists()}")
# print(f"Is file: {file_path.is_file()}")
#
# # Getting detailed stats (if the file exists)
# if file_path.exists():
#     stats = file_path.stat()
#     print(f"File size: {stats.st_size} bytes")
#     print(f"Last modified: {stats.st_mtime}")
#
#     # Access the st_ctime attribute for creation time (or last metadata change)
#     creation_timestamp = stats.st_ctime

#
#     # Convert the timestamp to a human-readable datetime object
#     creation_datetime =  datetime.datetime.fromtimestamp(creation_timestamp)
def get_metadata(file_path):
    a = file_path
    file_path = Path(file_path)
    if file_path.exists():
        stats = file_path.stat()
        last_modidied  = datetime.fromtimestamp(stats.st_mtime).strftime("%Y-%m-%d %H:%M:%S")
        creation_timestamp= datetime.fromtimestamp(stats.st_ctime).strftime("%Y-%m-%d %H:%M:%S")



        dic_data = {'Name': file_path.name ,
                    'Stem': file_path.stem ,
                    "Suffix": file_path.suffix,
                    "Parent": file_path.parent  ,
                    "File size": stats.st_size ,
                    "Last modified": last_modidied,
                    'creation_datetime' : creation_timestamp,
                    'file path with type': file_path ,
                    'file path' :   a

                    }
        return dic_data


    return "file not found"
# print(get_metadata(file_path ="podcasts\download (7).wav"))

import os

def get_file_paths_in_list(directory_path):

    file_paths = []
    for filename in os.listdir(directory_path):
        full_path = os.path.join(directory_path, filename)
        if os.path.isfile(full_path):  # Check if it's a file, not a subdirectory
            file_paths.append(full_path)
            print(full_path)
    return file_paths

# list_file  = get_file_paths_in_list(config.PATH_TO_DIRECTORY)
# for path in list_file:
#     print(get_metadata(path))
# # # Example usage:
# folder_to_scan = r"podcasts"  # Replace with your folder path
# file_list = get_file_paths_in_directory(folder_to_scan)
# # for file_path in file_list:
# #     print(file_path)

# Import Tinytag method from
# tinytag library
from tinytag import TinyTag

# Pass the filename into the
# Tinytag.get() method and store
# the result in audio variable
audio = TinyTag.get(r"C:\Users\1\Desktop\DATA_Analiza\podcasts\download (4).wav")

# Use the attributes
# and Display
print("Title:" + audio.title)
print("Artist: " + audio.artist)
print("Genre:" + audio.genre)
print("Year Released: " + audio.year)
print("Bitrate:" + str(audio.bitrate) + " kBits/s")
print("Composer: " + audio.composer)
print("Filesize: " + str(audio.filesize) + " bytes")
print("AlbumArtist: " + audio.albumartist)
print("Duration: " + str(audio.duration) + " seconds")
print("TrackTotal: " + str(audio.track_total))