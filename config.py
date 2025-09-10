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
            "transcription_audio" : {"type": "keyword"} ,
            "is_bds" : {"type": "boolean"} ,
            "bds_threat_level" : {"type": "keyword"}  ,
            "bds_percent" :{"type":  "double"}

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
# URI = os.getenv("URI" , "mongodb://localhost:27017")
URI = os.getenv("URI" , "mongodb://mongodb:27017")
COLLECTION_NAME = os.getenv("COLLECTION_NAME" , "test_collection")
SCHEMA_elastic = os.getenv("SCHEMA_ELASTIC" , 'http')
# HOST_ELASTIC = os.getenv("HOST_ELASTIC" , 'localhost')
HOST_ELASTIC = os.getenv("HOST_ELASTIC" , 'es')
PORT_ELASTIC = os.getenv("PORT_ELASTIC" , 9200)
LOGGER_PODCAST_INDEX_NAME = os.getenv("LOGGER_PODCAST_INDEX_NAME" , 'logger_podcast')
LOGGER_PODCAST_NAME = os.getenv("LOGGER_PODCAST_NAME" , 'logger_podcast')
NAME_TEMPORARY_WAV_PATH_FILE = os.getenv("NAME_TEMPORARY_WAV_PATH_FILE" , 'temporary.wav')
NAME_FIELD_TRANSCRIPTION_AUDIO = os.getenv("NAME_FIELD_TRANSCRIPTION_AUDIO" , 'transcription_audio')
THRESHOLD_DANGEROUS_WORD = os.getenv("THRESHOLD_DANGEROUS_VERY_DANGEROUS" , 0.025)
LIST_WORD_VERY_HOSTILE_STRING_BASE64 = os.getenv("LIST_WORD_VERY_HOSTILE_STRING_BASE64" ,'R2Vub2NpZGUsV2FyIENyaW1lcyxBcGFydGhlaWQsTWFzc2FjcmUsTmFrYmEsRGlzcGxhY2VtZW50LEh1bWFuaXRhcmlhbiBDcmlzaXMsQmxvY2thZGUsT2NjdXBhdGlvbixSZWZ1Z2VlcyxJQ0MsQkRT')
LIST_WORD_LESS_HOSTILE_STRING_BASE64 = os.getenv("LIST_WORD_LESS_HOSTILE_STRING_BASE64",'RnJlZWRvbSBGbG90aWxsYSxSZXNpc3RhbmNlLExpYmVyYXRpb24sRnJlZSBQYWxlc3RpbmUsR2F6YSxDZWFzZWZpcmUsUHJvdGVzdCxVTlJXQQ==')

VERY_DANGEROUS_WORS_SCORE = os.getenv("VERY_DANGEROUS_WORS_SCORE" , 2)
LESS_DANGEROUS_WORS_SCORE = os.getenv("LESS_DANGEROUS_WORS_SCORE" , 1)

NAME_FAILD_FOR_IS_BDS = os.getenv("NAME_FAILD_FOR_IS_BDS" , "is_bds")
NAME_FAILD_FOR_BDS_THREAT_LEVEL = os.getenv("NAME_FAILD_FOR_BDS_THREAT_LEVEL" , "bds_threat_level")
NAME_FAILD_FOR_BDS_PERCENT = os.getenv("NAME_FAILD_FOR_BDS_PERCENT" , "bds_percent")
REBOOT_TIME_TRANSCRIPTION  = os.getenv("REBOOT_TIME_transcription" , 600)
REBOOT_TIME_CALCULATION_PERCENTAGE_OF_DANGER = os.getenv("REBOOT_TIME_CALCULATION_PERCENTAGE_OF_DANGER" , 600)