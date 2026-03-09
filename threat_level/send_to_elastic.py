from elasticsearch import Elasticsearch
import os
from logger import Logger

logger = Logger.get_logger()

class SendingToElastic:
    def __init__(self):
        elastic_uri =  os.getenv("ELASTIC_URI", "http://elasticsearch:9200")
        self.es =Elasticsearch(elastic_uri)
        self.index_name = os.getenv("INDEX_NAME", "podcasts_metadata")
    
    def update_elastic(self, doc_id, bds_percent, is_bds, bds_threat_level):
        try:
            body = {"doc": {
                        "bds_percent": bds_percent,
                        "is_bds": is_bds,
                        "bds_threat_level": bds_threat_level}} 
                
            self.es.update(index=self.index_name, id=doc_id, body=body)
            logger.info(f"Successfully updated document {doc_id} in index {self.index_name}")
            return True
        except Exception as e:
            logger.error(f"Failed to update document {doc_id}: {e}")
            return False