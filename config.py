import os

index_mapping = {
    "mappings": {
        "properties": {
            "Name": {"type": "keyword"},
            "Stem": {"type": "keyword"},
            "Suffix": {"type": "keyword"},
            "Parent": {"type": "keyword"},
            "File size": {"type": "integer"},
            "Last modified": {"type": "keyword"},
            "creation_datetime": {"type": "keyword"} ,
            "file path with type": {"type": "keyword"} ,
            "file path": {"type": "keyword"} ,

        }
    }
}
PATH_TO_DIRECTORY =os.getenv('PATH_TO_DIRECTORY' , r"..\..\podcasts" )
UNIQUE_FIELD_INDENTIFIER_IN_JSON = os.getenv('UNIQUE_FIELD_INDENTIFIER_IN_JSON' , 'Name')
PATH_KEY_IN_DOC  = os.getenv('PATH_KEY_IN_DOC' , 'file path')
NAME_KEY_IN_DOC  = os.getenv('NAME_KEY_IN_DOC' , 'Name')
SIZE_NAME_IN_DOC = os.getenv("SIZE_NAME_IN_DOC" , "File size")
TOPIC_FOR_KAFKA = os.getenv('TOPIC_FOR_KAFKA' ,'mata_data_of_podcast')
INDEX_NAME = os.getenv("INDEX_NAME" , 'meta_data_podcast')
INDEX_MAPPING = os.getenv("MAPPING" , index_mapping)
DB_NAME = os.getenv("DB_NAME" ,"test_db")
URI = os.getenv("URI" , "mongodb://localhost:27017")
COLLECTION_NAME = os.getenv("COLLECTION_NAME" , "test_collection")
SCHEMA_elastic = os.getenv("SCHEMA_ELASTIC" , 'http')
HOST_ELASTIC = os.getenv("HOST_ELASTIC" , 'localhost')
PORT_ELASTIC = os.getenv("PORT_ELASTIC" , 9200)
LOGGER_PODCAST_INDEX_NAME = os.getenv("LOGGER_PODCAST_INDEX_NAME" , 'logger_podcast')
LOGGER_PODCAST_NAME = os.getenv("LOGGER_PODCAST_NAME" , 'logger_podcast')