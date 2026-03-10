from elasticsearch import Elasticsearch
import os
from logger import Logger

logger = Logger.get_logger()

class ThreatData:
    def __init__(self):
        elastic_uri =  os.getenv("ELASTIC_URI", "http://elasticsearch:9200")
        self.es = Elasticsearch(elastic_uri)
        self.index_name = os.getenv("INDEX_NAME", "podcasts_metadata")


    def execute_query(self, query):
        try:
            threats = self.es.search(index=self.index_name, query=query, size=1000)
            results = []
            hits = threats["hits"]["hits"]
            for hit in hits:
                results.append(hit["_source"])
            logger.info(f"Query successful. Retrieved {len(results)} items.")
            return results
        except Exception as e:
            logger.error(f"Failed to execute query on {self.index_name}. Error: {str(e)}")
            return []
    

    def get_all_threats(self):
        query = {"match_all": {}}
        result = self.execute_query(query)
        return result
    
    def get_threats_by_level(self, level: str):
        query = {"match": {"bds_threat_level": level}}
        result = self.execute_query(query)
        return result
    
    def get_podcast_text_by_name(self, name: str):
        query = {"term": {"name.keyword": name}}
        result = self.execute_query(query)
        return result[0].get("transcript")
    
    def search_word_in_transcript(self, word: str):
        query = {"match": {"transcript": word}}
        result = self.execute_query(query)
        return result