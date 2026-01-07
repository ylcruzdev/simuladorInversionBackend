from fastapi import Request
from fastapi.responses import JSONResponse
from app.core.exceptions import CryptoNotFoundError, ExternalAPIError

def crypto_not_found_handler(request: Request, exc: CryptoNotFoundError):
    return JSONResponse(
        status_code=404,
        content={
            "error": "CRYPTO_NOT_FOUND",
            "message": str(exc)
        }
    )

def external_api_error_handler(request: Request, exc: ExternalAPIError):
    return JSONResponse(
        status_code=503,
        content={
            "error": "EXTERNAL_API_ERROR",
            "message": str(exc)
        }
    )
