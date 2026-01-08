from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
from app.core.security import SECRET_KEY, ALGORITHM
from app.services.users import getUserByEmail

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

async def getCurrentUser(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email = payload.get("sub")
        if not email:
            raise HTTPException(status_code=401)
    except JWTError:
        raise HTTPException(status_code=401)

    user = await getUserByEmail(email)
    if not user:
        raise HTTPException(status_code=401)

    return user