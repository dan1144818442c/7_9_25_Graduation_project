from pymongo import MongoClient
class Dal_mongo:
    def __init__(self,uri,DB,collection):
        self.connection = MongoClient(uri)
        self.DB = self.connection[DB]
        self.collection = self.DB[collection]

    def insert(self,document , id  = None):
        if id:
            document["_id"] = id
        return self.collection.insert_one(document )


    def get_all_doc(self):
        docs = list(self.collection.find({}))
        for d in docs:
            d["_id"] = str(d["_id"])
        return docs