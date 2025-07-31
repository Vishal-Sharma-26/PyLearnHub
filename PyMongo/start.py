# import module
import pymongo

# Connect to MongoDB (default: localhost, port 27017)
client = pymongo.MongoClient("mongodb://localhost:27017/")


# Reference a database (created when data is added)
db = client["Employees"]  # Database named 'mydatabase'


# Reference a collection (created when data is added)
collection = db["EmployeesData"]  # Collection named 'mycollection'


# Insert a document to create the database and collection
document = {"name": "Alice", "age": 25, "city": "New York"}
result = collection.insert_one(document)
print(f"Inserted document with ID: {result.inserted_id}")


# Verify database creation
databases = client.list_database_names()
print("Databases:", databases)  # 'Employees' will appear after insertion


# Verify collection creation
collections = db.list_collection_names()
print("Collections in mydatabase:", collections)  # 'EmployeesData' will appear


# Close the connection
client.close()