import time
from kafkaconsumer import KafkaConsumer
from unique_id import UniqueId
from send_to_elastic import SendingToElastic
from mongo_client import ClientMongo


class Main:
    def __init__(self):
        self.kafka_consumer = KafkaConsumer()
        self.id_generator = UniqueId()
        self.elastic = SendingToElastic()
        self.mongo = ClientMongo()

    def process_task(self, metadata):
        try:
            updated_metadata = self.id_generator.add_id(metadata)
            uid = updated_metadata["uid"]
            file_path = updated_metadata.get("path")
            
            self.elastic.send(updated_metadata)

            if file_path:
                with open(file_path, "r", encoding="utf-8") as f:
                    content = f.read()
                self.mongo.save_file(uid, content)
        except Exception:
            pass   

    def run(self):
        try:
            while True:
                metadata = self.kafka_consumer.consume()
                if metadata:
                    self.process_task(metadata)
                time.sleep(0.1)
        finally:
            self.mongo.close()


if __name__ == "__main__":
    app = Main()
    app.run()