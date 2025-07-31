'''
PyMongo supports MongoDB’s powerful query operators for precise data retrieval.

A) Operators: Use $in, $nin, $exists, $regex, $elemMatch, etc., for complex queries.
B) Sorting and Limiting: Control result order and size with sort(), limit(), and skip().
'''

import pymongo
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["mydatabase"]
collection = db["mycollection"]

# Insert sample data
collection.insert_many([
    {"name": "Alice", "age": 25, "city": "New York", "hobbies": ["reading", "gaming"]},
    {"name": "Bob", "age": 30, "city": "London", "hobbies": ["painting"]},
    {"name": "Charlie", "age": 35, "city": "New York", "hobbies": ["gaming"]}
])

# Query with operators
# Find users in New York or London
results = collection.find({"city": {"$in": ["New York", "London"]}})
for doc in results:
    print(doc)

# Find users with a specific hobby
results = collection.find({"hobbies": {"$elemMatch": {"$eq": "gaming"}}})
for doc in results:
    print(doc)

# Regex query: Names starting with 'A'
results = collection.find({"name": {"$regex": "^A", "$options": "i"}})  # Case-insensitive
for doc in results:
    print(doc)

# Sort by age (descending) and limit to 2 results
results = collection.find().sort("age", pymongo.DESCENDING).limit(2)
for doc in results:
    print(doc)


'''
2) Bulk Operations

bulk_write(requests): Execute multiple write operations (insert, update, delete) efficiently in a single batch.
'''
from pymongo import InsertOne, UpdateOne, DeleteOne

# Prepare bulk operations
requests = [
    InsertOne({"name": "Dave", "age": 40, "city": "Paris"}),
    UpdateOne({"name": "Alice"}, {"$set": {"age": 26}}),
    DeleteOne({"name": "Bob"})
]

# Execute bulk write
result = collection.bulk_write(requests)
print(f"Inserted: {result.inserted_count}, Updated: {result.modified_count}, Deleted: {result.deleted_count}")


'''
3) Transactions

Multi-Document Transactions: PyMongo supports transactions for atomic operations across multiple documents/collections (requires MongoDB 4.0+ and replica sets).
'''
with client.start_session() as session:
    with session.start_transaction():
        # Insert into two collections atomically
        db["collection1"].insert_one({"name": "Eve", "balance": 100}, session=session)
        db["collection2"].insert_one({"transaction_id": "tx1", "amount": 100}, session=session)
        # Transaction commits automatically if no errors


'''
4) Change Streams

watch(): Monitor real-time changes to a collection (e.g., inserts, updates, deletes).
'''
# Watch for changes in the collection
with collection.watch() as stream:
    print("Listening for changes...")
    for change in stream:
        print(change)  # Prints change details (e.g., inserted document)
        break  # Stop after one change for demo


'''
5) Connection Pooling

PyMongo manages a connection pool automatically, but you can configure it for performance.
Options: maxPoolSize, minPoolSize, maxIdleTimeMS.
'''
# Configure connection pool
client = MongoClient("mongodb://localhost:27017/", maxPoolSize=50, minPoolSize=10)
# Pool maintains 10-50 connections


'''
6) Working with Indexes

create_indexes(): Create multiple indexes at once.
index_information(): View existing indexes.
'''
from pymongo import IndexModel, ASCENDING, DESCENDING

# Create multiple indexes
indexes = [
    IndexModel([("name", ASCENDING)], unique=True),
    IndexModel([("city", ASCENDING), ("age", DESCENDING)])
]
collection.create_indexes(indexes)

# View indexes
print(collection.index_information())


'''
7) GridFS for Large Files (Extended)

Store and retrieve large files (e.g., images, videos) efficiently.
'''
from gridfs import GridFS

fs = GridFS(db)

# Store a file
with open("sample_image.jpg", "rb") as file:
    file_id = fs.put(file, filename="sample_image.jpg")

# Retrieve and save file
with open("output_image.jpg", "wb") as output:
    output.write(fs.get(file_id).read())


'''
8) Database Commands

command(): Run MongoDB database commands (e.g., collStats, dbStats).
'''
# Get collection stats
stats = db.command("collStats", "mycollection")
print(stats)  # Prints collection statistics

# Get database stats
db_stats = db.command("dbStats")
print(db_stats)  # Prints database statistics


'''
9) Authentication

Connect to a MongoDB instance with authentication.
'''
# Connect with username and password
client = MongoClient("mongodb://username:password@localhost:27017/mydatabase?authSource=admin")


'''
10) Timeout Handling

Configure timeouts for operations to prevent hanging.
'''
# Set socket timeout and operation timeout
client = MongoClient("mongodb://localhost:27017/", connectTimeoutMS=5000, serverSelectionTimeoutMS=5000)

# Example with operation timeout
try:
    result = collection.find_one(timeout=2)  # Timeout after 2 seconds
    print(result)
except pymongo.errors.ServerSelectionTimeoutError:
    print("Operation timed out")


'''
A) Error Handling: Always wrap operations in try-except to handle network issues or invalid queries.
'''
try:
    collection.insert_one({"name": "Test"})
except pymongo.errors.DuplicateKeyError:
    print("Document with unique key already exists")


'''
B) Performance: Use indexes for frequent queries and limit fields with projections ({"name": 1, "_id": 0}).
C) MongoDB Atlas: For cloud-hosted MongoDB, use a connection string like:
D) PyMongo Documentation: Refer to the official PyMongo docs for detailed options.
'''
client = MongoClient("mongodb+srv://<username>:<password>@cluster0.mongodb.net/mydatabase")


'''
Closing the Connection

Always close the client to free resources:
'''
client.close()