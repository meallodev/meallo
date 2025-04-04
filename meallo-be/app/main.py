from fastapi import FastAPI, HTTPException, Depends
from app.database import users_collection, menu_collection
from bson import ObjectId
from bson import json_util
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import random
import string
import smtplib 
from twilio.rest import Client
import os
from dotenv import load_dotenv

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Change this to your frontend URL in production (e.g., "http://localhost:3000")
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all headers
)

TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
TWILIO_PHONE_NUMBER = os.getenv("TWILIO_PHONE_NUMBER")

client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

@app.get("/")
def read_root():
    return {"message": "Hello FastAPI"}


class User(BaseModel):
    name: str
    contactNumber: str

class VerifyOTP(BaseModel):
    contactNumber: str
    otp: str

@app.post("/addCustomer/")
async def add_document(user: User):
    result = await users_collection.insert_one(user.dict())
    return {"inserted_id": str(result.inserted_id)}

def generate_otp():
    return str(random.randint(100000, 999999))  # Generates a 6-digit OTP

@app.post("/submit-form")
def submit_form(user: User):
    otp = generate_otp()
    users_collection.update_one({"contactNumber": user.contactNumber}, {"$set": {"otp": otp}}, upsert=True)
    print(f"OTP for {user.contactNumber}: {otp}")  # Replace with Twilio SMS sending logic
    return {"message": "OTP sent to your contactNumber"}

# @app.post("/submit-form")
# def submit_form(user: User):
#     otp = generate_otp()

#     # Store user details & OTP in MongoDB
#     users_collection.update_one(
#         {"contactNumber": user.contactNumber},
#         {"$set": {"name": user.name, "otp": otp}},
#         upsert=True
#     )

#     # Twilio SMS sending logic
#     try:
#         message = client.messages.create(
#             body=f"Hello {user.name}, your OTP is: {otp}",
#             from_=TWILIO_PHONE_NUMBER,
#             to=user.contactNumber
#         )
#         print(f"OTP sent to {user.contactNumber}: {otp}")
#         return {"message": "OTP sent successfully", "sid": message.sid}
#     except Exception as e:
#         print("Error sending OTP:", e)
#         return {"message": "Failed to send OTP", "error": str(e)}

@app.post("/verify-otp")
async def verify_otp(data: VerifyOTP):
    user = await users_collection.find_one({"contactNumber": data.contactNumber})
    
    if not user or user.get("otp") != data.otp:
        raise HTTPException(status_code=400, detail="Invalid OTP")
    
    return {"message": "OTP Verified", "redirect": "/menu"}

@app.get("/get-menu")
async def get_menu():
    menu_cursor = menu_collection.find({}, {"_id": 0})  # Exclude MongoDB ObjectID
    menu = await menu_cursor.to_list(length=None)  # ✅ Await and convert to list
    return {"menu": menu}
