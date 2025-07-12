from pymongo import MongoClient


class Conectar:
    def __init__(self):
        self.client = MongoClient()
        self.db = self.client["rh"]
        self.collection = self.db["cadastre"]

    def get_collection(self):
        return self.collection