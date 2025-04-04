from motor.motor_asyncio import AsyncIOMotorClient
from pymongo.server_api import ServerApi
import os

# MongoDB Atlas connection URI
MONGO_URI = os.getenv("MONGO_URI")
# Initialize MongoDB Client
client = AsyncIOMotorClient(MONGO_URI, server_api=ServerApi("1"))

# Select Database and Collection
db = client["test_restaurant"]  # Change this to your database name
users_collection = db["customer_data"]  # Change this to your collection name
menu_collection = db["menu"] 