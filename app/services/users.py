from app.models.user import User
from app.core.security import hashPassword, verifyPassword

async def getUserByEmail(email: str):
    return await User.find_one(User.email == email)

async def createUser(email: str, password: str):
    user = User(
        email=email,
        password=hashPassword(password)
    )
    await user.insert()
    return user

async def authenticateUser(email: str, password: str):
    user = await getUserByEmail(email)
    if not user:
        return None
    if not verifyPassword(password, user.password):
        return None
    return user