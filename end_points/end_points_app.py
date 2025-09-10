
from fastapi import FastAPI,Body, HTTPException
from Dal.Dal_Elastic import ElasticSerarch
import config
app = FastAPI()
INSTANS_ES = ElasticSerarch()


@app.post("/create_index/{index_name}")
async def create_index(index_name , mapping= Body(default=None)):
    INSTANS_ES.create_index(index_name=index_name ,index_mapping=mapping)

    return INSTANS_ES.es.indices.get_mapping(index=index_name)

@app.get("/ping")
async def ping():
    return INSTANS_ES.ping()

@app.delete("/delete_doc_with_risk_val/{risk_level}")
async def delete_doc_with_risk_val(risk_level):
    query = {
        "query": {
            "term": {
                config.NAME_FAILD_FOR_BDS_THREAT_LEVEL: risk_level
            }
        }
    }

    return INSTANS_ES.delete_by_query(index_name=config.INDEX_NAME , query=query)

# @app.post("/create_doc/{index_name}")
# async def create_doc(index_name ,doc = Body()):
#     return INSTANS_ES.create_doc(index_name=index_name ,doc=doc )

# @app.get("/get_all_doc/{index_name}")
# async def get_all_doc(index_name):
#     return INSTANS_ES.search(index_name=index_name , query={"match_all":{}})


@app.get("/get_all_doc_with_risk/{risk_level}")
async def get_all_doc_with_risk(risk_level):
    return INSTANS_ES.search(index_name=config.INDEX_NAME , query= { 'query': {'match': {config.NAME_FAILD_FOR_BDS_THREAT_LEVEL: risk_level}}})


@app.get("/search_by_id/{id}")
async def search_by_id(id):
    return INSTANS_ES.search_by_id(index_name=config.INDEX_NAME , id=id)


@app.get("/search_bds_percent/{more_or_less}/{number}")
async def search_bds_percent(more_or_less , number):
        if more_or_less == "more":
            body={
                'query': {
                    'range': {
                        config.NAME_FAILD_FOR_BDS_PERCENT: {
                            'gte': number
                        }
                    }
                }
            }
        else:
            body = {
                'query': {
                    'range': {
                        config.NAME_FAILD_FOR_BDS_PERCENT: {

                            'lte': number
                        }
                    }
                }
            }

        return INSTANS_ES.search(index_name=config.INDEX_NAME , query=body)


