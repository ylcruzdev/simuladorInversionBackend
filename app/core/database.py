from motor.motor_asyncio import AsyncIOMotorClient
from beanie import init_beanie
from app.models.user import User
import os

MONGO_URI = os.getenv("MONGO_URI", "mongodb://mongo:27017")
DB_NAME = os.getenv("DB_NAME", "crypto_db")

client = AsyncIOMotorClient(MONGO_URI)
db = client[DB_NAME]

async def initDB():
    await init_beanie(
        database=db,
        document_models=[User]
    )