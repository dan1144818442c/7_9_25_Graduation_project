from pymongo import MongoClient
import gridfs

import config



class Dal_mongo:
    def __init__(self,uri,DB,collection):
        self.connection = MongoClient(uri)
        self.DB = self.connection[DB]
        self.collection = self.DB[collection]
        self.fs = gridfs.GridFS(self.DB)

    def insert_file_wav(self,document , wav_file_path , id  = None ):

        with open(wav_file_path, 'rb') as f:
            file_id = self.fs.put(f, filename=document[config.NAME_KEY_IN_DOC], content_type='audio/wav')
            return file_id

    def get_all_doc(self):
        docs = list(self.collection.find({}))
        for d in docs:
            d["_id"] = str(d["_id"])
        return docs