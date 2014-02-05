import pymongo

from pymongo import MongoClient

connection = MongoClient('localhost', 27017)

# Create a connection to mongodb.
db = connection.test

# Connect to the test database.
names = db.test

# Retrieve a name from the names collection.
item = names.find_one()

# Print the name to the console.
print item['name']