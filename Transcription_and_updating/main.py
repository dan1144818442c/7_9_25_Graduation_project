from  logger_ import log
import config
from  DataPersister.persister import Persister
from tools import convert_wav

def transcription_and_updating_doc(field_name_for_Transcription  , mongo_fs , id  , doc_to_update):
    logger = log.Logger.get_logger()
    try:
        print(id)
        print(doc_to_update)
        binary_data = convert_wav.get_binary_data_from_mongo(mongo_fs=mongo_fs, id=id)
        text = convert_wav.transcription_from_binary_audio(binary_data=binary_data)
        doc_to_update[field_name_for_Transcription] = text
        print(doc_to_update)
        logger.info(f"transcription doc with this id - {id} successfully")
        return doc_to_update

    except Exception as e:
            logger.error(f"transcription doc with this id - {id} - {e}")

if __name__ == '__main__':
    logger = log.Logger.get_logger()
    persister = Persister(index_name=config.INDEX_NAME , mapping_for_elastic=config.INDEX_MAPPING , db_name=config.DB_NAME , uri=config.URI , collection_name="new")
    all_ids_mongo_files = persister.mongo.get_all_id_fro_collection()

    for id in all_ids_mongo_files:
        doc_to_update = persister.es.search_by_id(index_name=config.INDEX_NAME , id=id)
        if doc_to_update is None:
            logger.error(f"cant find the document with this id : {id} in elastic jast in mongo !")
        if  not (config.NAME_FIELD_TRANSCRIPTION_AUDIO in doc_to_update.keys()):
            doc_to_update = transcription_and_updating_doc(field_name_for_Transcription=config.NAME_FIELD_TRANSCRIPTION_AUDIO,mongo_fs=persister.mongo.fs , id=id , doc_to_update=doc_to_update)

        persister.es.update_doc(index_name=config.INDEX_NAME , doc=doc_to_update , id=id)
