import config
from  persister import Persister
from  kafka_.kafka_consumer import Subscriber

if __name__ == '__main__':

    persister = Persister(index_name=config.INDEX_NAME , mapping_for_elastic=config.INDEX_MAPPING , db_name=config.DB_NAME , uri=config.URI , collection_name="new")

    sub = Subscriber(topic=config.TOPIC_FOR_KAFKA)

    for message in sub.consumer:
        print(message.value)
        doc = message.value
        list_uniqe_fields = [doc[config.NAME_KEY_IN_DOC]  , doc[config.PATH_KEY_IN_DOC] , doc[config.SIZE_NAME_IN_DOC]]
        id  = Persister.get_new_id(uniq_fields=list_uniqe_fields)
        # print(id)
        persister.upload_to_elastic(message.value ,id_=id)
        persister.inser_file_wav_to_mongo(doc=message.value , path_to_file=message.value[config.PATH_KEY_IN_DOC] , id=id)



