from  logger_ import log
import config
from  DataPersister.persister import Persister
from tools import convert_wav

def transcription_and_updating_doc(field_name_for_Transcription , path_for_temporary_file , mongo_fs , id  , doc_to_update):
    logger = log.Logger.get_logger()
    try:
        print(id)
        print(doc_to_update)
        binary_data = convert_wav.get_binary_data_from_mongo(mongo_fs=mongo_fs, id=id)
        convert_wav.export_binary_data_to_wav_file(path_to_export=path_for_temporary_file, data=binary_data)
        text = convert_wav.transcription_from_wav_file(path_for_temporary_file)
        doc_to_update[field_name_for_Transcription] = text
        print(doc_to_update)
        logger.info(f"transcription doc with this id - {id} successfully")
        return doc_to_update

    except Exception as e:
            logger.error(f"transcription doc with this id - {id} - {e}")

if __name__ == '__main__':
    persister = Persister(index_name=config.INDEX_NAME , mapping_for_elastic=config.INDEX_MAPPING , db_name=config.DB_NAME , uri=config.URI , collection_name="new")
    all_ids_mongo_files = persister.mongo.get_all_id_fro_collection()

    for id in all_ids_mongo_files:
        doc_to_update = persister.es.search_by_id(index_name=config.INDEX_NAME , id=id)
        if  not (config.NAME_FIELD_TRANSCRIPTION_AUDIO in doc_to_update.keys()):
            doc_to_update = transcription_and_updating_doc(field_name_for_Transcription=config.NAME_FIELD_TRANSCRIPTION_AUDIO,path_for_temporary_file=config.NAME_TEMPORARY_WAV_PATH_FILE,mongo_fs=persister.mongo.fs , id=id , doc_to_update=doc_to_update)

        # print(doc_to_update)
        persister.es.update_doc(index_name=config.INDEX_NAME , doc=doc_to_update , id=id)
