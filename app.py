import streamlit as st
import matplotlib.pyplot as plt
from api import obtener_datos
from analisis import procesar

st.title("Farmacias de Turno en Chile")
st.caption("Datos obtenidos desde FARMANET - Ministerio de Salud")

datos = obtener_datos()
por_region, por_comuna, por_horario = procesar(datos)

st.subheader("Farmacias por Región")
region_sel = st.multiselect("Filtrar regiones", por_region["region"].tolist(), default=por_region["region"].tolist())
df_region = por_region[por_region["region"].isin(region_sel)]
fig, ax = plt.subplots()
ax.bar(df_region["region"], df_region["total"])
ax.set_xlabel("Región")
ax.set_ylabel("Total farmacias")
st.pyplot(fig)

st.subheader("Farmacias por Comuna")
comuna_sel = st.selectbox("Seleccionar comuna", por_comuna["comuna"].tolist())
df_comuna = por_comuna[por_comuna["comuna"] == comuna_sel]
st.metric("Total farmacias", int(df_comuna["total"].values[0]))

st.subheader("Horarios de Apertura más frecuentes")
fig2, ax2 = plt.subplots()
ax2.barh(por_horario["hora_apertura"], por_horario["total"])
ax2.set_xlabel("Total")
ax2.set_ylabel("Hora apertura")
st.pyplot(fig2)