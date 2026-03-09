import os
from logger import Logger
from decryption import Decryption
from reading_from_elastic import ReadingFromElastic
from calculation import Calculation
from send_to_elastic import SendingToElastic 

logger = Logger.get_logger()

class Main:
    def __init__(self):
        self.reading_from_elastic = ReadingFromElastic()
        self.decryption = Decryption()
        self.send_to_elastic = SendingToElastic()
        
        hostile_list = self.decryption.decode_text(os.getenv("HOSTILE_LIST_ENCODED"))
        very_hostile_list = self.decryption.decode_text(os.getenv("VERY_HOSTILE_LIST_ENCODED"))
        
        self.analyzer = Calculation(hostile_list, very_hostile_list)

    def run(self):
        logger.info("Starting processing cycle.")
        
        documents = self.reading_from_elastic.get_data_from_elastic()
        if not documents:
            logger.info("No documents found to process.")
            return

        for doc in documents:
            doc_id = doc['_id']
            text = doc['_source'].get('transcript', '')
            
            bds_percent, is_bds, bds_threat_level = self.analyzer.analyze_message(text)
            
            success = self.send_to_elastic.update_elastic(doc_id, bds_percent, is_bds, bds_threat_level)
            
            if success:
                logger.info(f"Processed doc {doc_id}: level={bds_threat_level}")
            else:
                logger.error(f"Failed to process doc {doc_id}")

if __name__ == "__main__":
    app = Main()
    app.run()