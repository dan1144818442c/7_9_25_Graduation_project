docker run --name mongodb  --network=mynetw -p 27017:27017 -d mongodb/mongodb-community-server:latest

docker run -d --name es -p 9200:9200 -e "discovery.type=single-node" -e "xpack.security.enabled=false" -e "ES_JAVA_OPTS=-Xms1g -Xmx1g" docker.elastic.co/elasticsearch/elasticsearch:8.15.0

docker run -d --name kibana -p 5601:5601 -e "ELASTICSEARCH_HOSTS=http://host.docker.internal:9200"    docker.elastic.co/kibana/kibana:8.15.0

docker run -d --name=kafka -p 9092:9092 apache/kafka
