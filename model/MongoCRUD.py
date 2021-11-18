# MongoDB Access and CRUD test

from pymongo import MongoClient

# 1.MongoDB Connection
client = MongoClient('localhost', 27017) # (IP address, Port number)
db = client['local']                     # Allocation 'local' DB
collection = db.get_collection('test')   # Allocating 'review' Collection

data = {'name': 'cherry', 'age': 8}
collection.insert_one(data)

# MongoDB > database > collection > document

# CRUD => Creat, Read, Update, Delete