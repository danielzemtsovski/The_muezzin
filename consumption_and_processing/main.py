import time
from kafkaconsumer import KafkaConsumer
from unique_id import UniqueId
from send_to_elastic import SendingToElastic
from mongo_client import ClientMongo
from logger import Logger

logger = Logger.get_logger()

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

            with open(file_path, "rb") as f:
                file_bytes = f.read()

            self.mongo.save_file(uid, file_bytes)
            
            self.elastic.send(updated_metadata)
            
            logger.info(f"Successfully processed and indexed task for UID: {uid}")
        except Exception as e:
            logger.error(f"Failed to process task: {type(e).__name__} - {str(e)}")   

    def run(self):
        try:
            logger.info("The muazin consumer started successfully")
            while True:
                metadata = self.kafka_consumer.consume()
                if metadata:
                    self.process_task(metadata)
                time.sleep(0.1)
        except Exception as e:
            logger.error(f"Critical error in main loop: {type(e).__name__} - {str(e)}")
        finally:
            self.mongo.close()


if __name__ == "__main__":
    app = Main()
    app.run()