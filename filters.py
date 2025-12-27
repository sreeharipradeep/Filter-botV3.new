from pymongo import MongoClient
from config import MONGO_URL  # Ensure MONGO_URL set in config.py

# Connect to MongoDB
client = MongoClient(MONGO_URL)
db = client["MovieFilterBot"]
filters_col = db["filters"]

# Add or update a filter
def add_filter(keyword, file_id):
    filters_col.update_one(
        {"keyword": keyword},
        {"$set": {"file_id": file_id}},
        upsert=True
    )

# Get filter by keyword
def get_filter(keyword):
    return filters_col.find_one({"keyword": keyword})
