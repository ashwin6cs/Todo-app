from pymongo import MongoClient
from urllib.parse import quote_plus
from pymongo import IndexModel, ASCENDING

# MongoDB connection parameters
username = "admin"
password = "test@123"
cluster_url = "cluster0.xrou7ul.mongodb.net"
# database_name = "your_database_name"  # Replace with your actual database name

# Escape username and password
escaped_username = quote_plus(username)
escaped_password = quote_plus(password)

# Construct the MongoDB connection URI
uri = f"mongodb+srv://{escaped_username}:{escaped_password}@{cluster_url}/?retryWrites=true&w=majority"

client = MongoClient(uri, connect=False)

db = client.todo_db

todo_collection = db["todo_collection"]

user_collection = db["user_collection"]

index_model = IndexModel([("user_name", ASCENDING)], unique=True)
user_collection.create_indexes([index_model])

profile_collection = db["profile_pic.files"]

index_model = IndexModel([("user_name", ASCENDING)], unique=True)
profile_collection.create_indexes([index_model])
