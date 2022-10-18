import pymongo
import os


import certifi
ca = certifi.where()

class MongodbOperation:

    def __init__(self) -> None:

        #self.client = pymongo.MongoClient(os.getenv('MONGO_DB_URL'),tlsCAFile=ca)
        self.client = pymongo.MongoClient("mongodb+srv://ravikanur:anitha*1969@cluster0.htuwoon.mongodb.net/test",tlsCAFile=ca)
        self.db_name="ineuron"

    def insert_many(self,collection_name,records:list):
        self.client[self.db_name][collection_name].insert_many(records)

    def insert(self,collection_name,record):
        self.client[self.db_name][collection_name].insert_one(record)
        
