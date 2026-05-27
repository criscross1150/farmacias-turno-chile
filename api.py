import requests

URL = "https://midas.minsal.cl/farmacia_v2/WS/getLocalesTurnos.php"

def obtener_datos():
    r = requests.get(URL)
    r.raise_for_status()
    return r.json()