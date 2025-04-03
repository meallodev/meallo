from motor.motor_asyncio import AsyncIOMotorClient
from pymongo.server_api import ServerApi
import os

# MongoDB Atlas connection URI
MONGO_URI = "mongodb+srv://07meallo:5Zm8hocijtZzdIGW@cluster0.uh3jrsl.mongodb.net/?retryWrites=true&w=majority"

# Initialize MongoDB Client
client = AsyncIOMotorClient(MONGO_URI, server_api=ServerApi("1"))

# Select Database and Collection
db = client["test_restaurant"]  # Change this to your database name
collection = db["customer_data"]  # Change this to your collection name
