import pandas as pd

def procesar(datos):
    df = pd.DataFrame(datos)

    por_region = df.groupby("RegionGlosa")["EstablecimientoCodigo"].count().reset_index()
    por_region.columns = ["region", "total"]

    por_tipo = df.groupby("TipoEstablecimientoGlosa")["EstablecimientoCodigo"].count().reset_index()
    por_tipo.columns = ["tipo", "total"]

    urgencia = df[df["TieneServicioUrgencia"] == "Si"].groupby("RegionGlosa")["EstablecimientoCodigo"].count().reset_index()
    urgencia.columns = ["region", "total"]

    return por_region, por_tipo, urgencia