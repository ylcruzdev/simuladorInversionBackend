from fastapi import FastAPI
from app.core.database import initDB
from app.routers import crypto, auth
from app.core.errorHandlers import (
    cryptoNotFoundHandler,
    externalApiErrorHandler
)
from app.core.exceptions import (
    CryptoNotFoundError,
    ExternalApiError
)

app = FastAPI()

@app.on_event("startup")
async def on_startup():
    await initDB()

app.add_exception_handler(CryptoNotFoundError, cryptoNotFoundHandler)
app.add_exception_handler(ExternalApiError, externalApiErrorHandler)

app.include_router(auth.router)
app.include_router(crypto.router)