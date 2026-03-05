import os
from confluent_kafka import Producer
import json
from logger import Logger

logger = Logger.get_logger()

class KafkaPublisher:
    def __init__(self):
        self.servers = os.getenv("KAFKA_URI", "kafka:9092")
        self.topic = os.getenv("KAFKA_TOPIC", "metadata_topic") 
        self.producer = Producer({'bootstrap.servers': self.servers})

    def delivery_report(self, err, msg):
        if err is not None:
            logger.error(f"Kafka delivery failed: {err}")
        else:
            logger.info(f"Message delivered to {msg.topic()} [{msg.partition()}]")

    def publish_raw(self, event_data):
        try:
            self.producer.produce(
                topic=self.topic, 
                value=json.dumps(event_data).encode('utf-8'),
                on_delivery=self.delivery_report)
            self.producer.poll(0)
        except Exception as e:
            logger.error(f"Error publishing to Kafka: {type(e).__name__} - {str(e)}")

    def finalize(self):
        self.producer.flush()
        logger.info("Kafka publisher flushed and finalized.")