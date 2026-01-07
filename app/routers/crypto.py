from fastapi import APIRouter
from app.services.coingecko import getCryptoPrice
from app.schemas.crypto import CryptoPriceResponse

router = APIRouter(
    prefix="/price",
    tags=["Crypto"]
)

@router.get("/{cryptoName}", response_model=CryptoPriceResponse)
def getPrice(cryptoName: str):
    price = getCryptoPrice(cryptoName)

    return {
        "crypto": cryptoName,
        "priceEur": price
    }