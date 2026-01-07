import requests
from app.core.exceptions import CryptoNotFoundError, ExternalAPIError

coinGeckoUrl = "https://api.coingecko.com/api/v3/simple/price"

def getCryptoPrice(cryptoName: str) -> float:
    params = {
        "ids": cryptoName,
        "vs_currencies": "eur"
    }

    try:
        response = requests.get(coinGeckoUrl, params=params, timeout=5)
    except requests.RequestException:
        raise ExternalAPIError("No se pudo conectar con CoinGecko")

    if response.status_code != 200:
        raise ExternalAPIError("Error en la respuesta de CoinGecko")

    data = response.json()

    if cryptoName not in data:
        raise CryptoNotFoundError(f"Cripto '{cryptoName}' no encontrada")

    return data[cryptoName]["eur"]