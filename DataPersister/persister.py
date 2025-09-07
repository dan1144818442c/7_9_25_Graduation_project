from tools.tools import Tools
from Dal_Elastic import ElasticSerarch
from Dal_mongodb import Dal_mongo
import uuid

class Persister:
    def __init__(self , index_name , mapping_for_elastic  , uri ,db_name , collection_name):
        self.mongo = Dal_mongo(uri,db_name,collection_name)
        self.es = ElasticSerarch()
        self.index_name = index_name
        self.es.create_index(index_name=index_name,index_mapping=mapping_for_elastic)



    @staticmethod
    def get_new_id():
        return str(uuid.uuid4())

    def upload_to_elastic(self , doc , id_ = None):
        self.es.create_doc(index_name=self.index_name, doc=doc , id=id_)

    def inser_doc_to_mongo(self , doc , id):
        self.mongo.insert(doc)

# a = Persister()
# for i in range(10):
#     print(Persister.get_new_id())