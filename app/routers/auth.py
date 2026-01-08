from fastapi import APIRouter, HTTPException
from app.schemas.auth import UserCreate, UserLogin, TokenResponse
from app.services.users import createUser, authenticateUser, getUserByEmail
from app.core.security import createAccessToken

router = APIRouter(
    prefix="/auth",
    tags=["Auth"]
)

@router.post("/register")
async def register(user: UserCreate):
    existing = await getUserByEmail(user.email)
    if existing:
        raise HTTPException(status_code=400, detail="Usuario ya existe")

    await createUser(user.email, user.password)
    return {"message": "Usuario creado correctamente"}

@router.post("/login", response_model=TokenResponse)
async def login(user: UserLogin):
    authUser = await authenticateUser(user.email, user.password)
    if not authUser:
        raise HTTPException(status_code=401, detail="Credenciales inválidas")

    token = createAccessToken({"sub": authUser["email"]})

    return {
        "accessToken": token,
        "tokenType": "bearer"
    }