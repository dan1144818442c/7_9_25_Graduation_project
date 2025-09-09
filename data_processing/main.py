from  tools import tools
import config
from logger_ import log
from  DataPersister.persister import Persister
def calculating_percentage_of_danger(text , list_word , dangerous_word_score):
    counter = 0
    split_text = text.split(" ")
    for  word in list_word:

        if word in split_text:
            counter += dangerous_word_score

    return (counter / len(split_text))

def  level_danger_text(dangerous_score  , threshold_dangerousword ):
    if dangerous_score > (threshold_dangerousword *2) :
        return "high"
    if  dangerous_score <=0 :
        return "none"
    return "medium"


if __name__ == '__main__':
    list_word_very_hostile = tools.convert_string_to_list_word(tools.convert_bas64_to_string( 'R2Vub2NpZGUsV2FyIENyaW1lcyxBcGFydGhlaWQsTWFzc2FjcmUsTmFrYmEsRGlzcGxhY2VtZW50LEh1bWFuaXRhcmlhbiBDcmlzaXMsQmxvY2thZGUsT2NjdXBhdGlvbixSZWZ1Z2VlcyxJQ0MsQkRT'))
    list_word_less_hostile = tools.convert_string_to_list_word(tools.convert_bas64_to_string( 'RnJlZWRvbSBGbG90aWxsYSxSZXNpc3RhbmNlLExpYmVyYXRpb24sRnJlZSBQYWxlc3RpbmUsR2F6YSxDZWFzZWZpcmUsUHJvdGVzdCxVTlJXQQ=='))
    print(list_word_less_hostile)
    print(list_word_very_hostile)
    persister = Persister(index_name=config.INDEX_NAME , mapping_for_elastic=config.INDEX_MAPPING , db_name=config.DB_NAME , uri=config.URI , collection_name="new")
    logger = log.Logger.get_logger()
    all_ids_mongo_files = persister.mongo.get_all_id_fro_collection()
    c = 0
    for id in all_ids_mongo_files:
        c+= 1
        doc_to_update = persister.es.search_by_id(index_name=config.INDEX_NAME, id=id)
        if doc_to_update is None:
            logger.error(f"cant find the document with this id : {id} in elastic jast in mongo !")
            continue
        if  config.NAME_FIELD_TRANSCRIPTION_AUDIO in doc_to_update.keys():
            text = doc_to_update[config.NAME_FIELD_TRANSCRIPTION_AUDIO]
            percentage_of_danger_less_dangerous_word = calculating_percentage_of_danger(text , list_word=list_word_less_hostile , dangerous_word_score= 1)
            percentage_of_danger_very_dangerous_word = calculating_percentage_of_danger(text , list_word=list_word_very_hostile , dangerous_word_score= 2)
            print(percentage_of_danger_very_dangerous_word)
            dangerous_score = percentage_of_danger_less_dangerous_word + percentage_of_danger_very_dangerous_word
            level_danger = level_danger_text(dangerous_score=dangerous_score ,threshold_dangerousword= config.THRESHOLD_DANGEROUS_WORD)
            if level_danger == 'none':
                doc_to_update['is_bds'] = False
            else:
                doc_to_update["is_bds"] = True

            doc_to_update['bds_threat_level'] = level_danger
            if level_danger != 'medium':
                print(level_danger)
            doc_to_update['bds_percent'] = dangerous_score

            print(level_danger)
        persister.es.update_doc(index_name=config.INDEX_NAME, doc=doc_to_update, id=id)
    print(c)


