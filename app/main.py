from fastapi import FastAPI
from app.routers import crypto
from app.core.errorHandlers import (
    crypto_not_found_handler,
    external_api_error_handler
)
from app.core.exceptions import (
    CryptoNotFoundError,
    ExternalAPIError
)

app = FastAPI()

app.add_exception_handler(CryptoNotFoundError, crypto_not_found_handler)
app.add_exception_handler(ExternalAPIError, external_api_error_handler)

app.include_router(crypto.router)