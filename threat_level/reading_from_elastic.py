from elasticsearch import Elasticsearch
import os
from logger import Logger

logger = Logger.get_logger()

class ReadingFromElastic:
    def __init__(self):
        elastic_uri =  os.getenv("ELASTIC_URI", "http://elasticsearch:9200")
        self.es = Elasticsearch(elastic_uri)
        self.index_name = os.getenv("INDEX_NAME", "podcasts_metadata")


    def get_data_from_elastic(self):
        query = {"query": {"match_all": {}}}
        logger.info(f"Starting to load data from index: {self.index_name}")
        try:
            response = self.es.search(index=self.index_name, body=query, size=1000)
            hits = response['hits']['hits']
            logger.info(f"Successfully loaded {len(hits)} documents")
            return hits
        except Exception as e:
            logger.error(f"Failed to load data: {str(e)}")
            return []