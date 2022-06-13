from interfaces.ConnectorContentA import ConnectorContentA
from pymongo import MongoClient
class MongoConnector(ConnectorContentA):
    connectionString = None
    client           = None
    database         = None
    collection       = None
    def __init__(self, connectionString,databaseName, collectionName):
        self.connectionString = connectionString
        self.collectionName   = collectionName
        self.databaseName     = databaseName

    def connect(self):
        self.client = MongoClient(self.connectionString, authMechanism='SCRAM-SHA-256')
        if(self.client is not  None):
            return True
        return False

    def run(self):
        database   = self.client[self.databaseName]
        collection = database[self.collectionName]
        #for document in collection.find():
         #   pprint.pprint(document)
        count = collection.count_documents({})
        print(self.databaseName + " -> " + self.collectionName + " : " + str(count) + " documents")
        return True