from elasticsearch import Elasticsearch
import os

class SendingToElastic:
    def __init__(self):
        elastic_uri =  os.getenv("ELASTIC_URI")
        self.es =Elasticsearch(elastic_uri)
        self.index_name = "podcasts_metadata"

    def send(self, data):
        uid = data.get("uid")
        return self.es.index(
                index=self.index_name,
                id=uid,
                document=data)