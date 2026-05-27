import requests

URL = "https://midas.minsal.cl/farmacia_v2/WS/getLocalesTurnos.php"

HEADERS = {"User-Agent": "Mozilla/5.0"}

def obtener_datos():
    r = requests.get(URL, headers=HEADERS)
    r.raise_for_status()
    return r.json()