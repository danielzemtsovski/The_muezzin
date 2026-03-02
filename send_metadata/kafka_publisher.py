import os
from confluent_kafka import Producer
import json


class KafkaPublisher:
    def __init__(self):
        self.servers = os.getenv("KAFKA_URI", "kafka:9092")
        self.topic = os.getenv("KAFKA_TOPIC", "metadata_topic")
        
        self.producer = Producer({'bootstrap.servers': self.servers})

    def delivery_report(self, err, msg):
        if err is not None:
            print(f"Message delivery failed: {err}")
        else:
            print(f"Message delivered to {msg.topic()} [{msg.partition()}]")

    def publish_raw(self, event_data):
        self.producer.produce(
            topic=self.topic, 
            value=json.dumps(event_data).encode('utf-8'),
            on_delivery=self.delivery_report)
        self.producer.poll(0)

    def finalize(self):
        self.producer.flush() 