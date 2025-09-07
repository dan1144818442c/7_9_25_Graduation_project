from  kafka_ import kafka_consumer ,kafka_producer

def sub_and_pub( topic_to_listen):
    con = kafka_consumer.Subscriber(topic=topic_to_listen).consumer
    pub = kafka_producer.Produce()
    return con,pub

