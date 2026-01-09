from fastapi import Request
from fastapi.responses import JSONResponse
from app.core.exceptions import CryptoNotFoundError, ExternalApiError

def cryptoNotFoundHandler(request: Request, exc: CryptoNotFoundError):
    return JSONResponse(
        status_code = 404,
        content = {
            "error": "CRYPTO_NOT_FOUND",
            "message": str(exc)
        }
    )

def externalApiErrorHandler(request: Request, exc: ExternalApiError):
    return JSONResponse(
        status_code = 503,
        content={
            "error": "EXTERNAL_API_ERROR",
            "message": str(exc)
        }
    )