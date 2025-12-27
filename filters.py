from pymongo import MongoClient
from config import MONGO_URL

client = MongoClient(MONGO_URL)
db = client["MovieFilterBot"]
filters_col = db["filters"]

def add_filter(keyword, file_id):
    filters_col.update_one(
        {"keyword": keyword},
        {"$set": {"file_id": file_id}},
        upsert=True
    )

def get_filter(keyword):
    return filters_col.find_one({"keyword": keyword})
