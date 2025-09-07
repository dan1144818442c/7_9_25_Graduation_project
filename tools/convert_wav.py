
from bson.binary import Binary
import numpy as np
from scipy.io import wavfile

def get_binarry_of_wav_file(path_to_file):

    with open(path_to_file, 'rb') as f:
        wav_data = f.read()

    return Binary(wav_data)
def convert_binary_to_wav_file(path_to_save , binary_num):

    audio_array = np.frombuffer(binary_num, dtype=np.int16)
    # Save the NumPy array as a WAV file
    wavfile.write(path_to_save, 44100, audio_array)
