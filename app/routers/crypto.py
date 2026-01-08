from fastapi import APIRouter, Depends
from app.core.dependencies import getCurrentUser
from app.services.coingecko import getCryptoPrice
from app.schemas.crypto import CryptoPriceResponse

router = APIRouter(
    prefix="/price",
    tags=["Crypto"]
)

@router.get("/{cryptoName}", response_model=CryptoPriceResponse)
async def getPrice(cryptoName: str, currentUser=Depends(getCurrentUser) ):
    price = await getCryptoPrice(cryptoName)

    return {
        "crypto": cryptoName,
        "priceEur": price
    }