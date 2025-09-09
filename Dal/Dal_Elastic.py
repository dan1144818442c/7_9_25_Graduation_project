from elasticsearch import Elasticsearch
import config
from  logger_ import log
class ElasticSerarch:

    def __init__(self):
        self.es = Elasticsearch([{'scheme': config.SCHEMA_elastic, 'host': config.HOST_ELASTIC, 'port': config.PORT_ELASTIC}])
        self.logger = log.Logger.get_logger()
        self.update_connection_logging()


    def update_connection_logging(self):
        if self.ping():
            self.logger.info("The connection to ElasticSerarch was successfully connected.")
        else:
            self.logger.error("The connection to ElasticSerarch failed.")

    def ping(self):
        ping = self.es.ping()
        return ping

    def create_index(self, index_name, index_mapping=False):
        # Create index
        if not self.es.indices.exists(index=index_name):
            if index_mapping:
                self.es.indices.create(index=index_name, body=index_mapping)
                return "create by your mapping"
            self.es.indices.create(index=index_name)

            self.logger.info(f"create index - {index_name}")
            return "create index"

        self.logger.info(f"index = {index_name} already exists")
        return "already exists"

    def delete_index(self , index_name):
        try:
            if self.es.indices.exists(index=index_name):
                self.es.indices.delete(index=index_name)
                self.logger.info(f"Delete  index : '{index_name}' successfully ")
                return
        except Exception as e:
            self.logger.error(f"Faild Delete  index : '{index_name}' - {e}")


    def create_doc(self, index_name, doc , id ):
        try:
            respones = self.es.index(index= index_name, body= doc , id= id)
            if respones['result'] != 'created':
                self.logger.error( f"Faild add doc to  ELASTIC_SEARCH: {doc} with id : {id} , to index : {index_name}  - {e}")
                return respones
            self.logger.info(f"add doc to  ELASTIC_SEARCH: {doc} with id : {id} , to index : {index_name}")
            return respones

        except Exception as e:
            self.logger.error(f"Faild add doc to  ELASTIC_SEARCH: {doc} with id : {id} , to index : {index_name}  - {e}")

    #
    def search(self, index_name, query):
        response = self.es.search(
            index=index_name,
            body=query ,size=1000 )
        list_res = []
        for hit in response['hits']['hits']:
            list_res.append(hit)
        return list_res
    #
    #
    # def get_doc(self,index_name , id):
    #     doc = self.es.get(index=index_name, id=id)
    #     return doc['_source']
    #
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

    def search_by_id(self ,index_name,id):
        try:
            response = self.es.get(index=index_name, id=id)
            if response.get('found'):
                document = response.get('_source')
                return document
            else:
                self.logger.info(f"Document with ID '{id}' not found in index '{index_name}'.)")
        except Exception as e:
            self.logger.error(f"Document with ID '{id}' not found in index '{index_name}'  {e}")
    # def delete_doc(self , index_name , id = None , query = None):
    #     if not id and not  query:
    #         raise ValueError("must be id or query")
    #     elif id and query:
    #         raise ValueError("must be or  id or query")
    #     elif id and not query:
    #         self.es.delete(index=index_name , id=id)
    #     else:
    #         self.es.delete_by_query(index=index_name , body={'query' : query})
    #
    #     return "delete"


