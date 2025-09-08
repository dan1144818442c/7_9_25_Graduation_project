import config
from  persister import Persister
from  kafka_.kafka_consumer import Subscriber
import speech_recognition as sr

if __name__ == '__main__':

    persister = Persister(index_name=config.INDEX_NAME , mapping_for_elastic=config.INDEX_MAPPING , db_name=config.DB_NAME , uri=config.URI , collection_name="new")

    sub = Subscriber(topic=config.TOPIC_FOR_KAFKA)

    for message in sub.consumer:
        # print(message.value)
        doc = message.value
        list_uniqe_fields = [doc[config.NAME_KEY_IN_DOC]  , doc[config.PATH_KEY_IN_DOC] , doc[config.SIZE_NAME_IN_DOC]]
        id  = Persister.get_new_id(uniq_fields=list_uniqe_fields)
        # print(id)
        persister.upload_to_elastic(message.value ,id_=id)
        persister.inser_file_wav_to_mongo(doc=message.value , path_to_file=message.value[config.PATH_KEY_IN_DOC] , id=id)


        
        # wav_files_cursor = persister.mongo.fs._files.find({ })
        # filedname = config.NAME_KEY_IN_DOC
        # print(persister.mongo.fs._chunks.data)
        # for grid_out in persister.mongo.fs.find({}):
        #     print(f"Filename: {grid_out.filename}, Upload Date: {grid_out.uploadDate}")
        #     # You can also access other file properties like length, contentType, metadata, etc.
        #     data = grid_out.read() # To read the actual file content
        #     print(data)

        #
        #     r = sr.Recognizer()
        #     text = r.recognize_google(data)
        #     text = text.lower()
        #     print(text)
        # for grid_out in wav_files_cursor:
        #     print(grid_out)
        #
        #     # print(f"Found WAV file: {grid_out['filename']} (ID: {grid_out._id})")
        #
        #     # Read the file content
        #     file_content = grid_out.read()
        #
        #
        #     with open(f"downloaded_{grid_out['filename']}", "wb") as f:
        #         f.write(file_content)
        #
        #


