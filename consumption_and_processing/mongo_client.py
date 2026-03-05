import os
from pymongo import MongoClient


class ClientMongo:
    def __init__(self):
        self.mongo_uri = os.getenv("MONGO_URI")
        self.client = MongoClient(self.mongo_uri)
        self.db = self.client["muezzin_db"]
        self.collection = self.db["podcasts_txt"]

    def save_file(self, id, data):
        try:
            self.collection.update_one(
                {"_id": id},
                {"$set": {"content": data}},
                upsert=True)
        except Exception as e:
            print(f"Error: {e}")

    def close(self):
        self.client.close()