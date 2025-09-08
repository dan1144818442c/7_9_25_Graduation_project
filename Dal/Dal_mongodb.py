from pymongo import MongoClient
import gridfs
from logger_ import log
import config



class Dal_mongo:
    def __init__(self,uri,DB,collection):
        self.connection = MongoClient(uri)
        self.DB = self.connection[DB]
        self.collection = self.DB[collection]
        self.fs = gridfs.GridFS(self.DB)
        self.logger = log.Logger.get_logger()
        self.update_connection_logging()

    def update_connection_logging(self):
        if self.connection.db_name.command('ping') == {'ok': 1.0} :
            self.logger.info("The connection to MONGODB was successfully connected.")
        else:
            self.logger.info("The connection to MONGODB failed.")

    def insert_file_wav(self,document , wav_file_path , id  = None ):

        with open(wav_file_path, 'rb') as f:
            file_id = self.fs.put(f, filename=document[config.NAME_KEY_IN_DOC], content_type='audio/wav' , _id=id)
            return file_id

    def get_all_doc(self):
        docs = list(self.collection.find({}))
        for d in docs:
            d["_id"] = str(d["_id"])
        return docs

