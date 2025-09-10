from  tools import tools
import config
from logger_ import log
from  DataPersister.persister import Persister
import time
def calculating_percentage_of_danger(text, list_word, dangerous_word_score , logger):
    try:
        text = text.lower()
        words = text.split()
        total_words = len(words)
        score = 0

        joined_text = ' '.join(words)

        for term in list_word:
            term = term.lower()
            if ' ' in term:
                count = joined_text.count(term)
                print(term , count)
            else:
                count = words.count(term)
            score += count * dangerous_word_score
        logger.info(f"calculating percentage of danger for this  {text} on this list {list_word}")
        return (score / total_words) if total_words else 0
    except:
        logger.error( f"can't calculating percentage of danger for this  {text} on this list {list_word} ")



def  level_danger_text(dangerous_score  , threshold_dangerousword ):
    if dangerous_score > (threshold_dangerousword *2) :
        return "high"
    if  dangerous_score <= threshold_dangerousword /2 :
        return "none"
    return "medium"


def calculating_percentage_of_danger_and_add_field( ):

    list_word_very_hostile = tools.convert_string_to_list_word(tools.convert_bas64_to_string( config.LIST_WORD_VERY_HOSTILE_STRING_BASE64))
    list_word_less_hostile = tools.convert_string_to_list_word(tools.convert_bas64_to_string( config.LIST_WORD_LESS_HOSTILE_STRING_BASE64))
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
            percentage_of_danger_less_dangerous_word = calculating_percentage_of_danger(text , list_word=list_word_less_hostile , dangerous_word_score= config.LESS_DANGEROUS_WORS_SCORE , logger=logger)
            percentage_of_danger_very_dangerous_word = calculating_percentage_of_danger(text , list_word=list_word_very_hostile , dangerous_word_score= config.VERY_DANGEROUS_WORS_SCORE , logger=logger)
            print(percentage_of_danger_very_dangerous_word)
            dangerous_score = percentage_of_danger_less_dangerous_word + percentage_of_danger_very_dangerous_word
            level_danger = level_danger_text(dangerous_score=dangerous_score ,threshold_dangerousword= config.THRESHOLD_DANGEROUS_WORD)
            if level_danger == 'none':
                doc_to_update[config.NAME_FAILD_FOR_IS_BDS] = False
            else:
                doc_to_update[config.NAME_FAILD_FOR_IS_BDS] = True

            doc_to_update[config.NAME_FAILD_FOR_BDS_THREAT_LEVEL] = level_danger

            doc_to_update[config.NAME_FAILD_FOR_BDS_PERCENT] = dangerous_score

            print(level_danger)
        persister.es.update_doc(index_name=config.INDEX_NAME, doc=doc_to_update, id=id)
        logger.info(f"update this doc : { doc_to_update} in elastic with tis new fields :  1:{ config.NAME_FAILD_FOR_IS_BDS }  2: {config.NAME_FAILD_FOR_BDS_THREAT_LEVEL}  3: {config.NAME_FAILD_FOR_BDS_PERCENT}  ")

if __name__ == '__main__':

    while True:
        calculating_percentage_of_danger_and_add_field()
        time.sleep(600)




