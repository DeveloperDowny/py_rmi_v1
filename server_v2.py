import Pyro4
from pymongo import MongoClient
import mlib


@Pyro4.expose
class DatabaseServer:
    def __init__(self):
        
        self.client = MongoClient(mlib.mkey)
        self.db = self.client["mydatabase"]

    def insert_document(self, collection_name, document):
        
        collection = self.db[collection_name]
        result = collection.insert_one(document)
        return result.inserted_id

    def find_document(self, collection_name, query):
        
        collection = self.db[collection_name]
        result = list(collection.find(query))
        return result

def main():
    
    remote_object = DatabaseServer()

    
    with Pyro4.Daemon() as daemon:
        uri = daemon.register(remote_object)

        
        print("URI:", uri)

        
        daemon.requestLoop()

if __name__ == "__main__":
    main()
