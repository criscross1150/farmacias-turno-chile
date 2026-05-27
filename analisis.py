import pandas as pd

def procesar(datos):
    df = pd.DataFrame(datos)
    
    por_region = df.groupby("fk_region")["local_id"].count().reset_index()
    por_region.columns = ["region", "total"]
    
    por_comuna = df.groupby("comuna_nombre")["local_id"].count().reset_index()
    por_comuna.columns = ["comuna", "total"]
    
    por_horario = df.groupby("funcionamiento_hora_apertura")["local_id"].count().reset_index()
    por_horario.columns = ["hora_apertura", "total"]
    
    return por_region, por_comuna, por_horario