from elasticsearch import Elasticsearch
import config
class ElasticSerarch:

    def __init__(self):
        self.es = Elasticsearch([{'scheme': config.SCHEMA_elastic, 'host': config.HOST_ELASTIC, 'port': config.PORT_ELASTIC}])

    def ping(self):
        ping = self.es.ping()
        print(ping)
        return ping

    def create_index(self, index_name, index_mapping=False):
        # Create index
        if not self.es.indices.exists(index=index_name):
            if index_mapping:
                self.es.indices.create(index=index_name, body=index_mapping)
                return "create by your mapping"
            self.es.indices.create(index=index_name)
            return "create index"
        return "already exists"

    def delete_index(self , index_name):
        if self.es.indices.exists(index=index_name):
            self.es.indices.delete(index=index_name)


    def create_doc(self, index_name, doc , id ):
        respones = self.es.index(index=index_name, body=doc , id=id)
        return respones

    def search(self, index_name, query):

        response = self.es.search(
            index=index_name,
            body={'query':query} ,size=1000 )
        list_res = []
        for hit in response['hits']['hits']:
            list_res.append(hit)

        return list_res

    def get_doc(self,index_name , id):
        doc = self.es.get(index=index_name, id=id)
        return doc['_source']

    def update_doc(self , index_name, doc  , id = None  ,query =None):
        if not id and not  query:
            raise ValueError("must be id or query")
        elif id and query:
            raise ValueError("must be or  id or query")
        elif id and not query:
            self.es.update(index=index_name , id=id , body={'doc':doc})
        else:
            self.es.update_by_query(index=index_name , body={'query' : query , "doc"  :doc})
        return "update"

    def delete_doc(self , index_name , id = None , query = None):
        if not id and not  query:
            raise ValueError("must be id or query")
        elif id and query:
            raise ValueError("must be or  id or query")
        elif id and not query:
            self.es.delete(index=index_name , id=id)
        else:
            self.es.delete_by_query(index=index_name , body={'query' : query})

        return "delete"


