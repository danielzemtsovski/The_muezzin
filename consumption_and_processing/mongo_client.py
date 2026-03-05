import os
from pymongo import MongoClient
from logger import Logger

logger = Logger.get_logger()

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
            logger.info(f"document with ID: {id} saved to MongoDB")
        except Exception as e:
            logger.error(f"MongoDB Save Error for ID {id}: {type(e).__name__} - {str(e)}")

    def close(self):
        self.client.close()