from create_metadata import CreateMetadata
from files_path import FilesPath
from kafka_publisher import KafkaPublisher
import os
from logger import Logger
from speech_to_text import SpeechToText

logger = Logger.get_logger()

folder = os.getenv("FOLDER_PATH")

class Main:
    def __init__(self, folder_name):
        self.create_metadata = CreateMetadata()
        self.files_path = FilesPath(folder_name)
        self.kafka_publisher = KafkaPublisher()
        self.speech_to_text = SpeechToText()

    def run(self):
        try:
            logger.info(f"Starting metadata processing service for folder: {folder}")           
            files = self.files_path.get_all_paths()

            for file in files:
                try:
                    metadata = self.create_metadata.get_metadata(file)
                    file_path = metadata.get("path")
                    transcript = self.speech_to_text.audio_file_to_text(file_path)
                    metadata["transcript"] = transcript
                    logger.info(f"Transcript added to metadata for: {file.name}")
                    
                    self.kafka_publisher.publish_raw(metadata)
                    logger.info(f"Successfully processed and published: {metadata['name']}")
                except Exception as file_e:
                    logger.error(f"Error processing individual file {file}: {str(file_e)}")

            self.kafka_publisher.finalize()
            logger.info("Service run completed successfully.")

        except Exception as e:
            logger.error(f"Critical error in Main run: {type(e).__name__} - {str(e)}")

if __name__ == "__main__":
    app = Main(folder)
    app.run()