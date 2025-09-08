import speech_recognition as sr
from logger_ import log


def get_binary_data_from_mongo(mongo_fs , id):
    grid_out =mongo_fs.get(id)
    binary_data = grid_out.read()
    return binary_data

def export_binary_data_to_wav_file(path_to_export , data):
    with open(path_to_export, 'wb') as f:
        f.write(data)

def transcription_from_wav_file(path):
    r = sr.Recognizer()
    with sr.AudioFile(path) as audio:
        data = r.record(audio)
    text = r.recognize_google(data)
    return text

