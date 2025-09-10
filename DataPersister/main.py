import time

import config
from DataPersister.persister  import Persister
from  kafka_.kafka_consumer import Subscriber

if __name__ == '__main__':

    persister = Persister(index_name=config.INDEX_NAME , mapping_for_elastic=config.INDEX_MAPPING , db_name=config.DB_NAME , uri=config.URI , collection_name="new")

    sub = Subscriber(topic=config.TOPIC_FOR_KAFKA)

    for message in sub.consumer:
        print(message.value)
        doc = message.value
        list_uniqe_fields = [doc[config.NAME_KEY_IN_DOC]  , doc[config.PATH_KEY_IN_DOC] , doc[config.SIZE_NAME_IN_DOC]]
        id  = Persister.get_new_id(uniq_fields=list_uniqe_fields)
        persister.inser_file_wav_to_mongo(doc=doc, path_to_file=message.value[config.PATH_KEY_IN_DOC] , id=id)
        #     This part is if you want the transcription to be system-accelerated and not on its own.!!
        # data = convert_wav.get_binary_data_from_mongo(id=id , mongo_fs= persister.mongo.fs)
        # convert_wav.export_binary_data_to_wav_file(config.NAME_TEMPORARY_WAV_PATH_FILE , data=data)
        # text = convert_wav.transcription_from_wav_file(config.NAME_TEMPORARY_WAV_PATH_FILE)
        # doc["transcription_audio"] = text
        persister.upload_to_elastic(doc, id_=id)


