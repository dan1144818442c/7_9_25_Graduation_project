from kafka  import KafkaProducer
import json
from logger_ import log


class Produce:
    def __init__(self):
        self.logger = log.Logger.get_logger()
        try:
            self.producer = KafkaProducer(
                                    # bootstrap_servers=['localhost:9092'],
                                    bootstrap_servers=['broker:9092'],
                                     value_serializer=lambda x:
                                     json.dumps(x).encode('utf-8'))

            self.logger.info(f"Create producer   successfully ")

        except Exception as e:

            self.logger.error(f"Faild create producer - {e}")

    def publish_message(self,topic, message):
        try:
            self.producer.send(topic, message)
            self.producer.flush()
            self.logger.info(f"publish this message : {message} with this topic : {topic} successfully")

        except Exception as e:
            self.logger.error(f"Faild publish this message : {message} with this topic : {topic}  - {e}")
            return

