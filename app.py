import streamlit as st
import matplotlib.pyplot as plt
from api import obtener_datos
from analisis import procesar

st.title("Establecimientos de Salud en Chile")
st.caption("Datos obtenidos desde el Ministerio de Salud - datos.gob.cl")

datos = obtener_datos()
por_region, por_tipo, urgencia = procesar(datos)

st.subheader("Establecimientos por Región")
regiones = st.multiselect("Filtrar regiones", por_region["region"].tolist(), default=por_region["region"].tolist())
df_region = por_region[por_region["region"].isin(regiones)]
fig, ax = plt.subplots(figsize=(10, 5))
ax.bar(df_region["region"], df_region["total"])
ax.set_xlabel("Región")
ax.set_ylabel("Total")
plt.xticks(rotation=45, ha="right")
st.pyplot(fig)

st.subheader("Establecimientos por Tipo")
tipo_sel = st.selectbox("Seleccionar tipo", por_tipo["tipo"].tolist())
df_tipo = por_tipo[por_tipo["tipo"] == tipo_sel]
st.metric("Total establecimientos", int(df_tipo["total"].values[0]))

st.subheader("Establecimientos con Urgencia por Región")
fig2, ax2 = plt.subplots(figsize=(10, 5))
ax2.barh(urgencia["region"], urgencia["total"])
ax2.set_xlabel("Total")
ax2.set_ylabel("Región")
st.pyplot(fig2)