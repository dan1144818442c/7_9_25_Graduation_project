from Dal import Dal_Elastic
import config
from DataPersister import persister
# Generate a version 4 UUID (randomly generated)
# unique_id = uuid.uuid4()
# for i in range(10):
#
#     unique_id = uuid.uuid4()
# # Convert the UUID object to a string for storage in a database
#     unique_id_str = str(unique_id)
#
#     print(unique_id_str)
#
#
#from pymongo import MongoClient
# import gridfs
# import io
import speech_recognition as sr
#
#
es = Dal_Elastic.ElasticSerarch()
# print(es.ping())
# #
es.delete_index(index_name=config.INDEX_NAME)
# print(es.search(index_name=config.INDEX_NAME, query={"match_all": {}}))

#
# from pydub import AudioSegment
# from io import BytesIO
# from bson.binary import Binary
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
#     wavfile.write(path_to_save, 44100, audio_array)# Assume you have your binary WAV data
#
# b = get_binarry_of_wav_file(r"C:\Users\1\Desktop\DATA_Analiza\podcasts\download (7).wav")
# convert_binary_to_wav_file("abc.wav" , b)
# # # # Create a file-like object from the binary data
# # audio_stream = BytesIO(binary_wav_data)
# # #
# # # # Create an AudioSegment from the raw data (specify parameters if it's raw PCM)
# # # # Adjust format, frame_rate, channels, sample_width as per your data
# # audio_segment = AudioSegment.from_file(audio_stream, format='raw',
# #                                       frame_rate=44100, channels=1, sample_width=2)
# #
# # # Export the AudioSegment to a WAV file
# # output_filename = 'output.wav'
# # audio_segment.export(output_filename, format='wav')
#
# # audio_bytes = b
# # audio_segment = AudioSegment(
# #     data=audio_bytes,
# #     sample_width=2, # Sample width in bytes
# #     frame_rate=44100, # Frame rate
# #     channels=1 # Mono
# # )
# # audio_segment.export('output.wav', format='wav')
#
#
#
#
#
# # # Assume 'audio_bytes' contains the raw audio byte data
# # audio_bytes = b
# # # Convert bytes to a NumPy array
# # audio_array = np.frombuffer(audio_bytes, dtype=np.int16)
# # # Save the NumPy array as a WAV file
# # wavfile.write('output1.wav', 44100, audio_array)
persister = persister.Persister(index_name=config.INDEX_NAME, mapping_for_elastic=config.INDEX_MAPPING, db_name=config.DB_NAME,
                      uri=config.URI,collection_name="A")
# print(persister.mongo.get_all_id_fro_collection())
# wav_files_cursor = persister.mongo.fs._files.find({ })
# filedname = config.NAME_KEY_IN_DOC
# print(persister.mongo.fs._chunks.data)
# for grid_out in persister.mongo.fs.find({}):
#     print(f"Filename: {grid_out.filename}, Upload Date: {grid_out.uploadDate}")
#     # You can also access other file properties like length, contentType, metadata, etc.
#     data = grid_out.read() # To read the actual file content
#     print(type(data))
#     bytes_data =data
#     import base64
#
#     base64_string = data
#     decoded_data = base64.b64decode(base64_string)
#     import wave
#
#     output_filename = "output_audio.wav"
#     # These parameters must match the original audio data encoded in Base64
#     nchannels = 1  # Number of audio channels (e.g., 1 for mono, 2 for stereo)
#     sampwidth = 2  # Sample width in bytes (e.g., 2 for 16-bit audio)
#     framerate = 44100  # Sample rate in Hz (e.g., 44100 Hz)
#
#     with wave.open(output_filename, 'wb') as wav_file:
#         wav_file.setnchannels(nchannels)
#         wav_file.setsampwidth(sampwidth)
#         wav_file.setframerate(framerate)
#         wav_file.writeframes(decoded_data)

import base64
# grid_out =persister.mongo.fs.get(889638274)
# binary_data = grid_out.read()
# base64_encoded_data = base64.b64encode(binary_data)
# base64_string = base64_encoded_data.decode('utf-8')
# print(base64_string)
# import speech_recognition as sr
#
# import wave
# decoded_data = base64.b64decode(base64_string)
# output_filename = "output_audio.wav"

# If the decoded data is raw PCM, you'll need to specify parameters like
# number of channels, sample width, and sample rate.
# For example, for 1-channel, 16-bit PCM at 44100 Hz:
# with wave.open(output_filename, 'wb') as wf:
#     wf.setnchannels(1)
#     wf.setsampwidth(2) # 2 bytes for 16-bit
#     wf.setframerate(44100)
#     wf.writeframes(decoded_data)

# If the base64 string already represents a complete WAV file,
# you can directly write the decoded data:
# with open(output_filename, 'wb') as f:
#     f.write(binary_data)
# # r = sr.Recognizer()
#
# text = r.recognize_google(base64_string)
# text = text.lower()

# from tools import convert_wav
# data = convert_wav.get_binary_data_from_mongo(persister.mongo.fs , 158776080)
# convert_wav.export_binary_data_to_wav_file("abc.wav" , data)
from  tools import convert_wav
import io
data = convert_wav.get_binary_data_from_mongo(persister.mongo.fs, -97809700)
