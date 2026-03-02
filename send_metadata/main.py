from create_metadata import CreateMetadata
from files_path import FilesPath
from kafka_publisher import KafkaPublisher

class Main:
    def __init__(self, folder_name):
        self.create_metadata = CreateMetadata()
        self.files_path = FilesPath(folder_name)
        self.kafka_publisher = KafkaPublisher()

    def run(self):            
        files = self.files_path.get_all_paths()
        for file in files:
            metadata = CreateMetadata.get_metadata(file)
            print(f"Publishing metadata for: {metadata['name']}")

            self.kafka_publisher.publish_raw(metadata)
        self.kafka_publisher.finalize()

if __name__ == "__main__":
    app = Main("podcasts")
    app.run()