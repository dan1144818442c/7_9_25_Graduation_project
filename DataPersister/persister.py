from Dal.Dal_Elastic import ElasticSerarch
from Dal.Dal_mongodb import Dal_mongo
from logger_ import log


class Persister:
    def __init__(self , index_name , mapping_for_elastic  , uri ,db_name , collection_name):
        self.mongo = Dal_mongo(uri,db_name,collection_name)
        self.es = ElasticSerarch()
        self.index_name = index_name
        self.es.create_index(index_name=index_name,index_mapping=mapping_for_elastic)
        self.logger = log.Logger.get_logger()


    @staticmethod
    def get_new_id(uniq_fields):
        uniqe_val = 1
        for field in uniq_fields:
           uniqe_val *=  hash(str(field))
        return int(str(uniqe_val)[:9])

    def upload_to_elastic(self , doc , id_ = None):

        self.es.create_doc(index_name=self.index_name, doc=doc , id=id_)

    def inser_file_wav_to_mongo(self , doc ,path_to_file, id):
        id =self.mongo.insert_file_wav(doc , wav_file_path= path_to_file , id=id)
        return id

    def get_all_doc(self):
        return self.mongo.get_all_doc()


    #     self.mongo.get_all_wav_file()