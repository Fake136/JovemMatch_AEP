from pymongo import MongoClient
from src.config import MONGO_URI, DATABASE_NAME

_client = None


def get_client():
    global _client
    if _client is None:
        _client = MongoClient(MONGO_URI, serverSelectionTimeoutMS=5000)
    return _client


def get_database():
    return get_client()[DATABASE_NAME]


def close_connection():
    global _client
    if _client is not None:
        _client.close()
        _client = None
