# create a database connection to a mongodb database which can be used across multiple  process host and port are in credentials.py file


import pymongo
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure

class DB:

    def __init__(self, host, port, db_name):
        self.host = host
        self.port = port
        self.db_name = db_name
        self.client = None
        self.db = None

    def connect(self):
        try:
            self.client = MongoClient(self.host, self.port)
            print("Connected successfully to MongoDB")
        except ConnectionFailure as e:
            print("Could not connect to MongoDB: %s" % e)

        self.db = self.client[self.db_name]

    def get_client(self):
        return self.client

    def get_db(self):
        return self.db

    def close(self):
        self.client.close()