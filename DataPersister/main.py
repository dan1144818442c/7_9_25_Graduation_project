import config
from  persister import Persister
from  kafka_.kafka_consumer import Subscriber
if __name__ == '__main__':

    persister = Persister(index_name=config.INDEX_NAME , mapping_for_elastic=config.INDEX_MAPPING , db_name=config.DB_NAME , uri=config.URI , collection_name=config.COLLECTION_NAME)

    sub = Subscriber(topic=config.TOPIC_FOR_KAFKA)

    for message in sub.consumer:
        print(message.value)
        id  = Persister.get_new_id()
        persister.upload_to_elastic(message.value ,id_=id)
        persister.inser_doc_to_mongo(message.value  , id=id)



