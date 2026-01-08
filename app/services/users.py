from app.core.database import userCollection
from app.core.security import hashPassword, verifyPassword

async def getUserByEmail(email: str):
    return await userCollection.find_one({"email": email})

async def createUser(email: str, password: str):
    user = {
        "email": email,
        "password": hashPassword(password)
    }
    await userCollection.insert_one(user)
    return user

async def authenticateUser(email: str, password: str):
    user = await getUserByEmail(email)
    if not user:
        return None
    if not verifyPassword(password, user["password"]):
        return None
    return user