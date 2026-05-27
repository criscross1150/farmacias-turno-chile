import requests

URL = "https://datos.gob.cl/api/3/action/datastore_search"
RESOURCE_ID = "2c44d782-3365-44e3-aefb-2c8b8363a1bc"

def obtener_datos():
    registros = []
    offset = 0
    limit = 1000

    while True:
        params = {"resource_id": RESOURCE_ID, "limit": limit, "offset": offset}
        r = requests.get(URL, params=params)
        r.raise_for_status()
        resultado = r.json()["result"]
        registros.extend(resultado["records"])
        if offset + limit >= resultado["total"]:
            break
        offset += limit

    return registros