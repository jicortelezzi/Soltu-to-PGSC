# app.py
import pandas as pd
import streamlit as st

# Load data
@st.cache_data
def load_data():
    return pd.read_csv("resultado_sequencias.csv")

df = load_data()

# Web interface
st.title("🧬 Soltu–PGSC Gene ID Converter")
st.write("Ingresá un ID de gen y obtené su correspondencia entre las nomenclaturas **Soltu** y **PGSC** junto con el valor E.")

# Selection: query type
query_type = st.radio("Seleccioná el tipo de búsqueda:", ["Buscar por Soltu ID", "Buscar por PGSC ID"])

# Input
user_input = st.text_input("Ingresá el ID:")

# Process
if user_input:
    if query_type == "Buscar por Soltu ID":
        match = df[df['soltu_id'] == user_input]
        if not match.empty:
            row = match.iloc[0]
            st.success(f"**PGSC ID:** `{row['pgsc_id']}`\n\n**E-value:** `{row['evalue']}`")
        else:
            st.error("Soltu ID no encontrado.")
    else:
        match = df[df['pgsc_id'] == user_input]
        if not match.empty:
            row = match.iloc[0]
            st.success(f"**Soltu ID:** `{row['soltu_id']}`\n\n**E-value:** `{row['evalue']}`")
        else:
            st.error("PGSC ID no encontrado.")

# Credits
st.markdown("---")
st.markdown(
    "🧬 Developed by **Juan Ignacio Cortelezzi** at the "
    "[Plant Genetic Engineering Laboratory (INGEBI, CONICET)](https://ingebi-conicet.gov.ar/es_ingenieria-genetica-de-plantas/).",
    unsafe_allow_html=True
)