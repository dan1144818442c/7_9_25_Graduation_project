from kafka  import KafkaConsumer
import json
from logger_ import log

class Subscriber:
    def __init__(self,topic):
        self.logger = log.Logger.get_logger()
        try:
            self.consumer = KafkaConsumer(topic,
                value_deserializer=lambda m: json.loads(m.decode('ascii')),
                bootstrap_servers=['localhost:9092'])

            self.logger.info(f"Create consumer with topic :{topic}  successfully ")

        except Exception as e:

            self.logger.error(f"Faild create consumer with topic :{topic}  successfully   - {e}")


