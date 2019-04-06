from pymongo import MongoClient
from constants import DB_NAME, DB_COLLECTION


class Database:

    def __init__(self):
        self.client = MongoClient()
        self.db = self.client[DB_NAME]
        self.collection = self.db[DB_COLLECTION]

    def get_media(self, content_type, num, tag):
        if tag:
            return self.collection.find({"type": content_type, "tags": {"$in": [tag]}}).limit(num)
        return self.collection.find({"type": content_type}).limit(num)

    def get_overall(self, num, tag):
        if tag:
            return self.collection.find({"tags": {"$in": [tag]}}).limit(num)
        return self.collection.find().limit(num)

    def save(self, list_of_post):
        self.collection.insert_many(list_of_post)
