'''
Below is a concise overview of key PyMongo methods for interacting with MongoDB, along with code examples for each.
PyMongo is the Python driver for MongoDB, and these methods are commonly used for CRUD operations, querying, aggregation, and more.
The examples assume a MongoDB instance is running locally and a basic understanding of MongoDB concepts like databases and collections.
'''
import pymongo
from pymongo import MongoClient
from bson.objectid import ObjectId

# Connect to MongoDB (default: localhost, port 27017)
client = MongoClient("mongodb://localhost:27017/")
db = client["mydatabase"]  # Database
collection = db["mycollection"] # Collection


'''
1) Connection and Setup Methods

A) MongoClient(host, port): Establishes a connection to MongoDB.
B) client[database_name]: Accesses or creates a database.
C) db[collection_name]: Accesses or creates a collection.
'''
# Connect and create database/collection
client = MongoClient("mongodb://localhost:27017/")
db = client["mydatabase"]
collection = db["mycollection"]


'''
2) Insert Methods

A) insert_one(document): Inserts a single document.
B) insert_many(documents): Inserts multiple documents.
'''
# Insert one document
result = collection.insert_one({"name": "Alice", "age": 25, "city": "New York"})
print(result.inserted_id)  # Prints the ObjectId of the inserted document

# Insert multiple documents
documents = [
    {"name": "Bob", "age": 30, "city": "London"},
    {"name": "Charlie", "age": 35, "city": "Paris"},
    {"name": "John", "age": 25, "city": "USA"},
    {"name": "Emma", "age": 28, "city": "New York"},
    {"name": "Tom", "age": 40, "city": "Germany"}
]
result = collection.insert_many(documents)
print(result.inserted_ids)  # Prints list of ObjectIds


'''
3) Query Methods

A) find_one(filter, projection): Returns the first matching document.
B) find(filter, projection): Returns a cursor for all matching documents.
C) count_documents(filter): Counts documents matching the filter.
'''
# Find one document
result = collection.find_one({"name": "Alice"})
print(result)  # Prints the document, e.g., {'_id': ObjectId(...), 'name': 'Alice', ...}

# Find multiple documents
cursor = collection.find({"age": {"$gt": 25}})
for doc in cursor:
    print(doc)  # Prints all documents where age > 25

# Count documents
count = collection.count_documents({"city": "New York"})
print(count)  # Prints number of matching documents


'''
4) Update Methods

A) update_one(filter, update, upsert=False): Updates the first matching document.
B) update_many(filter, update, upsert=False): Updates all matching documents.
C) replace_one(filter, replacement, upsert=False): Replaces the first matching document.
'''
# Update one document
collection.update_one({"name": "Alice"}, {"$set": {"age": 26}})
# Document with name "Alice" now has age 26

# Update multiple documents
collection.update_many({"city": "New York"}, {"$set": {"country": "USA"}})
# All New York documents get country: "USA"

# Replace one document
collection.replace_one({"name": "Bob"}, {"name": "Bob", "age": 31, "city": "Berlin"})
# Replaces Bob's document entirely


'''
5) Delete Methods

A) delete_one(filter): Deletes the first matching document.
B) delete_many(filter): Deletes all matching documents.
'''
# Delete one document
collection.delete_one({"name": "Alice"})
# Removes the first document with name "Alice"

# Delete multiple documents
collection.delete_many({"city": "London"})
# Removes all documents with city "London"


'''
6) Aggregation

A) aggregate(pipeline): Executes an aggregation pipeline for advanced data processing.
'''
# Group documents by city and count
pipeline = [
    {"$group": {"_id": "$city", "count": {"$sum": 1}}}
]
results = collection.aggregate(pipeline)
for result in results:
    print(result)  # Prints e.g., {'_id': 'New York', 'count': 2}


'''
7) Index Management

A) create_index(keys, options): Creates an index to optimize queries.
B) drop_index(index_name): Drops a specific index.
'''
# Create an index on the "name" field
collection.create_index([("name", pymongo.ASCENDING)])
# Optimizes queries on the "name" field

# Drop an index
collection.drop_index("name_1")  # Drops the index on "name"


'''
8) GridFS for Large Files

A) GridFS(db): Manages large files by splitting them into chunks.
'''
from gridfs import GridFS

# Initialize GridFS
fs = GridFS(db)

# Store a file
with open("Intro.txt", "rb") as file:
    file_id = fs.put(file, filename="Intro.txt")
print(file_id)  # Prints the file's ObjectId

# Retrieve a file
file = fs.get(file_id)
print(file.read())  # Reads the file content


'''
9) Other Useful Methods

A) distinct(key): Returns unique values for a field.
B) drop(): Drops the entire collection.
C) list_collection_names(): Lists all collections in the database.
'''
# Get distinct values
cities = collection.distinct("city")
print(cities)  # Prints unique city values, e.g., ['New York', 'London']

# Drop collection
collection.drop()  # Deletes the collection

# List collections
collections = db.list_collection_names()
print(collections)  # Prints list of collection names


'''
Notes:

a) Error Handling: Use try-except blocks to handle connection errors or invalid queries.
'''
try:
    result = collection.find_one({"name": "Alice"})
    print(result)
except pymongo.errors.ConnectionError:
    print("Failed to connect to MongoDB")


'''b) Filters: Use operators like $gt, $lt, $in, $regex for advanced queries.'''
# Example: Find documents with age between 20 and 30
cursor = collection.find({"age": {"$gte": 20, "$lte": 30}})


'''c) Connection Closure: Close the client when done to free resources.'''
client.close()