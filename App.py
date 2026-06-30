import streamlit as st
import joblib
import gdown
import os

# 1. Descargar Modelo
url_modelo = 'https://drive.google.com/file/d/19xoi1Tr5KgDTS66paiuimCwHCwY-JB0/view?usp=sharing'
out_modelo = 'modelo_futbol.pkl'
if not os.path.exists(out_modelo):
    gdown.download(url_modelo, out_modelo, quiet=False, use_cookies=False)

# 2. Descargar Codificador (¡Es vital!)
url_cod = 'AQUÍ_VA_EL_ENLACE_DE_TU_CODIFICADOR_EN_DRIVE'
out_cod = 'codificador.pkl'
if not os.path.exists(out_cod):
    gdown.download(url_cod, out_cod, quiet=False, use_cookies=False)

# 3. Cargar ambos
modelo = joblib.load(out_modelo)
codificador = joblib.load(out_cod)

st.title("⚽ Predictor de Fútbol")
st.write("¡Modelo cargado correctamente!")


