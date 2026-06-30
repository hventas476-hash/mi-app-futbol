import streamlit as st
import joblib
import gdown
import os

# 1. Descargar Modelo
url_modelo = 'https://drive.google.com/file/d/19xoi1Tr5KgDTS66paiuimCwHCwY-JB0/view?usp=sharing'
out_modelo = 'modelo_futbol.pkl'
if not os.path.exists(out_modelo):
    gdown.download(url_modelo, out_modelo, quiet=False, use_cookies=False)

# 2. Descargar Codificador
# AQUÍ PEGA EL ENLACE QUE COPIASTE DEL PASO 1
url_cod = 'https://drive.google.com/file/d/1DjGjbOqI57KdFBz_2UT2m5ujVRiOUQaj/view?usp=drivesdk' 
out_cod = 'codificador.pkl'
if not os.path.exists(out_cod):
    gdown.download(url_cod, out_cod, quiet=False, use_cookies=False)

# 3. Cargar ambos
modelo = joblib.load(out_modelo)
codificador = joblib.load(out_cod)

st.title("⚽ Predictor de Fútbol")
st.write("¡Modelo y codificador cargados correctamente!")

