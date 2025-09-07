import uuid
from  DataPersister import Dal_Elastic
import numpy as np
from scipy.io import wavfile
import config
# Generate a version 4 UUID (randomly generated)
unique_id = uuid.uuid4()
for i in range(10):

    unique_id = uuid.uuid4()
# Convert the UUID object to a string for storage in a database
    unique_id_str = str(unique_id)

    print(unique_id_str)



field1 = "apple"
field2 = "red"
#
# # Option 1: Concatenation
# unique_id_concat = f"{field1}-{field2}"
# print(f"Concatenated ID: {unique_id_concat}")
#
# # Option 2: Hashing the combination
# import hashlib
#
# combined_string = f"{field1}-{field2}"
# unique_id_hash = hashlib.sha256(combined_string.encode()).hexdigest()
# print(f"Hashed ID: {unique_id_hash}")
es = Dal_Elastic.ElasticSerarch()

print(len(es.search(index_name=config.INDEX_NAME, query={"match_all": {}})))


from pydub import AudioSegment
from io import BytesIO
from bson.binary import Binary
with open(r"C:\Users\1\Desktop\DATA_Analiza\podcasts\download (7).wav", 'rb') as f:
    wav_data = f.read()

b = Binary(wav_data)
# print(b)
# Assume you have your binary WAV data
binary_wav_data = b  # Replace with your actual binary data
#
# # # Create a file-like object from the binary data
# audio_stream = BytesIO(binary_wav_data)
# #
# # # Create an AudioSegment from the raw data (specify parameters if it's raw PCM)
# # # Adjust format, frame_rate, channels, sample_width as per your data
# audio_segment = AudioSegment.from_file(audio_stream, format='raw',
#                                       frame_rate=44100, channels=1, sample_width=2)
#
# # Export the AudioSegment to a WAV file
# output_filename = 'output.wav'
# audio_segment.export(output_filename, format='wav')

# audio_bytes = b
# audio_segment = AudioSegment(
#     data=audio_bytes,
#     sample_width=2, # Sample width in bytes
#     frame_rate=44100, # Frame rate
#     channels=1 # Mono
# )
# audio_segment.export('output.wav', format='wav')




# Assume 'audio_bytes' contains the raw audio byte data
audio_bytes = b
# Convert bytes to a NumPy array
audio_array = np.frombuffer(audio_bytes, dtype=np.int16)
# Save the NumPy array as a WAV file
wavfile.write('output1.wav', 44100, audio_array)