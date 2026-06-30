import streamlit as st
import joblib
import gdown # Esta librería descarga archivos de Drive
import os 
# Enlace de tu archivo en Drive (el que copiaste)
url_modelo = 'https://drive.google.com/file/d/19xoL1Tr5KgDT566paLuimCwHCzWY-JbO/view?usp=drivesdk'
output = 'modelo_futbol.pkl'

# Descargar si no existe
if not os.path.exists(output):
    gdown.download(url_modelo, output, quiet=False)

# Cargar el modelo
modelo = joblib.load('modelo_futbol.pkl')

st.title("⚽ Predictor de Fútbol")
# ... resto de tu código de Streamlit ...

