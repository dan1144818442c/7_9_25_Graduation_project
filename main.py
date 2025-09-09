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
# persister = persister.Persister(index_name=config.INDEX_NAME, mapping_for_elastic=config.INDEX_MAPPING, db_name=config.DB_NAME,
#                       uri=config.URI,collection_name="A")
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
# from  tools import convert_wav
# import io
# data = convert_wav.get_binary_data_from_mongo(persister.mongo.fs, -97809700)
data = "R2Vub2NpZGUSV2FyIENyaW1lcyxBcGFydGhlaWQs TWFzc2FjcmUsTmFrYmEsRG1zcGxhY2VtZW50LEh1bWFuaXRhcmlhbiBDcmlzaXMsQmxvY2thZGUST2NjdXBhdGlvbixSZWZ1Z2V1cyxJQOMSQKRT"
# print()
# decoded_text = data.decode('utf-8')
# print(decoded_text)
# import base64

# import base64
#
# # The Base64 encoded string
# base64_encoded_string = "SGVsbG8gV29ybGQh"
#
# # Convert the Base64 string to bytes (using 'ascii' encoding is common for Base64)
# base64_bytes = base64_encoded_string.encode('ascii')
#
# # Decode the Base64 bytes into original bytes
# decoded_bytes = base64.b64decode(base64_bytes)
#
# # Convert the original bytes back to a string (using the appropriate encoding, e.g., 'utf-8')
# decoded_string = data.decode('utf-8')
#
# print(f"The decoded string is: {decoded_string}")
#

import base64

# The Base64-encoded string
base64_string ="R2Vub2NpZGUSV2FyIENyaW1lcyxBcGFydGhlaWQs TWFzc2FjcmUsTmFrYmEsRG1zcGxhY2VtZW50LEh1bWFuaXRhcmlhbiBDcmlzaXMsQmxvY2thZGUST2NjdXBhdGlvbixSZWZ1Z2V1cyxJQOMSQKRT"


# # 1. Convert the Base64 string to bytes (if it's not already)
# # This step is crucial because base64.b64decode expects bytes-like object
# base64_bytes = base64_string.encode('ascii')
#
# # 2. Decode the Base64 bytes
# decoded_bytes = base64.b64decode(base64_bytes)
#
# # 3. Convert the decoded bytes to a string (assuming original data was text)
# decoded_string = decoded_bytes.decode('utf-8')
#
# print(decoded_string)

# print(base64.b64decode(data))
from tools import tools
from DataPersister import persister
persister = persister.Persister(index_name=config.INDEX_NAME, mapping_for_elastic=config.INDEX_MAPPING, db_name=config.DB_NAME,
                      uri=config.URI, collection_name="new")

list_word_very_hostile = tools.convert_string_to_list_word(tools.convert_bas64_to_string(
    'R2Vub2NpZGUsV2FyIENyaW1lcyxBcGFydGhlaWQsTWFzc2FjcmUsTmFrYmEsRGlzcGxhY2VtZW50LEh1bWFuaXRhcmlhbiBDcmlzaXMsQmxvY2thZGUsT2NjdXBhdGlvbixSZWZ1Z2VlcyxJQ0MsQkRT'))
list_word_less_hostile = tools.convert_string_to_list_word(tools.convert_bas64_to_string(
    'RnJlZWRvbSBGbG90aWxsYSxSZXNpc3RhbmNlLExpYmVyYXRpb24sRnJlZSBQYWxlc3RpbmUsR2F6YSxDZWFzZWZpcmUsUHJvdGVzdCxVTlJXQQ=='))

search_values = list_word_very_hostile + ['last']
# print(search_values)
index_name = config.INDEX_NAME
field_name = "transcription_audio"
target_word = "of"

body = {
    "query": {
        "match": {
            field_name: target_word
        }
    },
    "aggs": {
        "word_count": {
            "terms": {
                "field": f"{field_name}.keyword", # Use .keyword for exact term matching
                "include": [target_word]
            }
        }
    }
}


# # Execute the search query
# response = persister.es.search(index_name=config.INDEX_NAME, query=body)
# if "aggregations" in response and "word_count" in response["aggregations"]:
#     buckets = response["aggregations"]["word_count"]["buckets"]
#     for bucket in buckets:
#         if bucket["key"] == target_word:
#             print(f"The word '{target_word}' appears {bucket['doc_count']} times.")
# # Replace 'your_index_name'

# Process the results
print(response)