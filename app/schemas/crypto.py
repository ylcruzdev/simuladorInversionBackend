from pydantic import BaseModel

class CryptoPriceResponse(BaseModel):
    crypto: str
    priceEur: float | None
