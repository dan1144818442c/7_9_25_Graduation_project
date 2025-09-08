
from bson.binary import Binary
import numpy as np
from scipy.io import wavfile
import base64

def get_binary_data_from_mongo(mongo_fs , id):
    grid_out =mongo_fs.get(id)
    binary_data = grid_out.read()
    return binary_data

def export_binary_data_to_wav_file(path_to_export , data):
    with open(path_to_export, 'wb') as f:
        f.write(data)

#
# def get_binarry_of_wav_file(path_to_file):
#
#     with open(path_to_file, 'rb') as f:
#         wav_data = f.read()
#
#     return Binary(wav_data)
# def convert_binary_to_wav_file(path_to_save , binary_num):
#
#     audio_array = np.frombuffer(binary_num, dtype=np.int16)
#     # Save the NumPy array as a WAV file
#     wavfile.write(path_to_save, 44100, audio_array)

    # import io
    #
    # # Create an in-memory text buffer
    # in_memory_file = io.StringIO()
    #
    # # Write data to the in-memory file
    # in_memory_file.write("This is line 1.\n")
    # in_memory_file.write("This is line 2.\n")
    #
    # # Get the content of the in-memory file
    # content = in_memory_file.getvalue()
    # print(content)
    #
    # # You can also read from it like a file
    # in_memory_file.seek(0) # Reset pointer to the beginning
    # line1 = in_memory_file.readline()
    # print(line1)