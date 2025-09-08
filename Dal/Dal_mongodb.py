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
            self.logger.error("The connection to MONGODB failed.")

    def insert_file_wav(self,document , wav_file_path , id  = None ):
        try:
            with open(wav_file_path, 'rb') as f:
                file_id = self.fs.put(f, filename=document[config.NAME_KEY_IN_DOC], content_type='audio/wav' , _id=id)

            self.logger.info(f"insert to mongo db - db name : {self.DB} , collection : {self.fs}  this document : {document} successfully ")

        except:
            self.logger.error(f"faild toinsert to mongo db - db name : {self.DB} , collection : {self.fs}  this document : {document}" )

    def get_all_doc(self):
        try:
            docs = list(self.collection.find({}))
            for d in docs:
                d["_id"] = str(d["_id"])
            self.logger.info(f"Pulling all DOCUMNET from MONGODB - db - db name : {self.DB} , collection : {self.fs}  successfully  ")
            return docs
        except:
            self.logger.error(f"Faild Pulling all DOCUMNET from MONGIDB db - db name : {self.DB} , collection : {self.fs}  successfully ")


    def get_all_id_fro_collection(self ):
        file_ids = []
        for grid_out in self.fs.find():
            file_ids.append(grid_out._id)
        return file_ids
    # def get_all_wav_file(self):
