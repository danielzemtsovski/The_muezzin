from elasticsearch import Elasticsearch
import os
from logger import Logger

logger = Logger.get_logger()

class SendingToElastic:
    def __init__(self):
        elastic_uri =  os.getenv("ELASTIC_URI", "http://elasticsearch:9200")
        self.es =Elasticsearch(elastic_uri)
        self.index_name = os.getenv("INDEX_NAME", "podcasts_metadata")

    def send(self, data):
        try:
            uid = data.get("uid")
            res = self.es.index(
                index=self.index_name,
                id=uid,
                document=data)
            logger.info(f"Successfully indexed metadata in Elastic for UID: {uid}")
            return res
        except Exception as e:
            logger.error(f"Failed to send data to Elastic: {type(e).__name__} - {str(e)}")
            return None