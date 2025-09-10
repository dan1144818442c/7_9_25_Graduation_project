
docker network create mynetw

docker  network  ls

docker run --name mongodb  --network=mynetw -p 27017:27017 -d mongodb/mongodb-community-server:latest

docker run -d --name es -p 9200:9200   --network=mynetw -e "discovery.type=single-node" -e "xpack.security.enabled=false" -e "ES_JAVA_OPTS=-Xms1g -Xmx1g"  docker.elastic.co/elasticsearch/elasticsearch:8.15.0

docker run -d --name kibana --network=mynetw -p 5601:5601 -e "ELASTICSEARCH_HOSTS=http://host.docker.internal:9200"    docker.elastic.co/kibana/kibana:8.15.0

docker run -d --name broker -p 9092:9092 -e KAFKA_NODE_ID=1 -e KAFKA_PROCESS_ROLES=broker,controller -e KAFKA_LISTENERS=PLAINTEXT://:9092,CONTROLLER://:9093 -e KAFKA_ADVERTISED_LISTENERS=PLAINTEXT://broker:9092 -e KAFKA_CONTROLLER_LISTENER_NAMES=CONTROLLER -e KAFKA_LISTENER_SECURITY_PROTOCOL_MAP=CONTROLLER:PLAINTEXT,PLAINTEXT:PLAINTEXT -e KAFKA_CONTROLLER_QUORUM_VOTERS=1@broker:9093 -e KAFKA_OFFSETS_TOPIC_REPLICATION_FACTOR=1 -e KAFKA_TRANSACTION_STATE_LOG_REPLICATION_FACTOR=1 -e KAFKA_TRANSACTION_STATE_LOG_MIN_ISR=1 -e KAFKA_GROUP_INITIAL_REBALANCE_DELAY_MS=0 -e KAFKA_NUM_PARTITIONS=3 --network mynetw apache/kafka:latest

docker build -t image_extract_data_v2 -f extracted_data/Dockerfile .

docker build -t image_data_presister_15 -f DataPersister/Dockerfile .

docker run --name con_data_persuster_v16  -e "PATH_TO_DIRECTORY=/app/podcasts" -v "C:\Users\1\Desktop\DATA_Analiza\podcasts":"/app/podcasts" --network=mynetw -d image_data_presister_15
docker run  --name con_extraxt_data_v4  --network=mynetw -d -e "PATH_TO_DIRECTORY=/app/podcasts" -v "C:\Users\1\Desktop\DATA_Analiza\podcasts":"/app/podcasts" image_extract_data_v2

docker build -t image_transcripition_v4 -f Transcription_and_updating/Dockerfile .

docker run --name con_transcripition_v4 --network=mynetw -d image_transcripition_v4

docker build -t image_data_processing_v3 -f data_processing/Dockerfile .

docker run --name con_data_processing_v3 --network=mynetw -d image_data_processing_v3

docker build -t image_fast_api_v3 -f end_points/Dockerfile .

docker run --name con_fastapi_v8 -p 8000:8000  --network=mynetw -d image_fast_api_v3
