from confluent_kafka import Consumer
import json
import os

kafka_uri = os.getenv("KAFKA_URI", "localhost:9092") 
kafka_topic= os.getenv("KAFKA_TOPIC", "metadata_topic")

class KafkaConsumer:
    def __init__(self):
        self.consumer = Consumer({
            'bootstrap.servers': kafka_uri,
            'group.id': 'metadata_consumer_group',
            'auto.offset.reset': 'earliest'})
        
        self.consumer.subscribe([kafka_topic])

    def consume(self):
        msg = self.consumer.poll(1.0)
        if msg is None:
            return None
        if msg.error():
            print("❌ Error:", msg.error())
            return None
        try:
            value = msg.value().decode("utf-8")
            return json.loads(value)
        except Exception as e:
            print(f"❌ JSON Decode Error: {e}")
            return None




