import uuid
from  DataPersister import Dal_Elastic
import config
# Generate a version 4 UUID (randomly generated)
unique_id = uuid.uuid4()
for i in range(10):

    unique_id = uuid.uuid4()
# Convert the UUID object to a string for storage in a database
    unique_id_str = str(unique_id)

    print(unique_id_str)



field1 = "apple"
field2 = "red"
#
# # Option 1: Concatenation
# unique_id_concat = f"{field1}-{field2}"
# print(f"Concatenated ID: {unique_id_concat}")
#
# # Option 2: Hashing the combination
# import hashlib
#
# combined_string = f"{field1}-{field2}"
# unique_id_hash = hashlib.sha256(combined_string.encode()).hexdigest()
# print(f"Hashed ID: {unique_id_hash}")
es = Dal_Elastic.ElasticSerarch()
print(es.search(index_name=config.INDEX_NAME, query={"match_all": {}}))