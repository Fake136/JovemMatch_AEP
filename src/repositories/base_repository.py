from typing import List, Optional, Dict, Any
from bson import ObjectId
from src.database import get_database


class BaseRepository:
    def __init__(self, collection_name: str):
        self.db = get_database()
        self.collection = self.db[collection_name]

    def insert(self, data: Dict[str, Any]) -> str:
        if "_id" in data and not data["_id"]:
            del data["_id"]
        result = self.collection.insert_one(data)
        return str(result.inserted_id)

    def find_by_id(self, id: str) -> Optional[Dict[str, Any]]:
        try:
            doc = self.collection.find_one({"_id": ObjectId(id)})
            if doc:
                doc["_id"] = str(doc["_id"])
            return doc
        except Exception:
            return None

    def find_all(self, filtro: Optional[Dict[str, Any]] = None) -> List[Dict[str, Any]]:
        filtro = filtro or {}
        docs = list(self.collection.find(filtro))
        for doc in docs:
            doc["_id"] = str(doc["_id"])
        return docs

    def update(self, id: str, data: Dict[str, Any]) -> bool:
        if "_id" in data:
            del data["_id"]
        result = self.collection.update_one({"_id": ObjectId(id)}, {"$set": data})
        return result.modified_count > 0

    def delete(self, id: str) -> bool:
        result = self.collection.delete_one({"_id": ObjectId(id)})
        return result.deleted_count > 0

    def count(self, filtro: Optional[Dict[str, Any]] = None) -> int:
        filtro = filtro or {}
        return self.collection.count_documents(filtro)

    def delete_all(self) -> int:
        result = self.collection.delete_many({})
        return result.deleted_count
