from fastapi import FastAPI
from app.database import collection
from bson import ObjectId
from bson import json_util

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello FastAPI"}


# Insert a document
@app.post("/add/")
async def add_document(data: dict):
    result = await collection.insert_one(data)
    return {"inserted_id": str(result.inserted_id)}

# Fetch all documents
@app.get("/documents/")
async def get_documents():
    documents = await collection.find().to_list(100)
    return json_util.dumps(documents)

# Fetch a document by ID
@app.get("/document/{doc_id}")
async def get_document(doc_id: str):
    document = await collection.find_one({"_id": ObjectId(doc_id)})
    if document:
        document["_id"] = str(document["_id"])
    return document or {"error": "Document not found"}
