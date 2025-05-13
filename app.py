# app.py
import pandas as pd
import streamlit as st

# Load data
@st.cache_data
def load_data():
    df = pd.read_csv("resultado_sequencias.csv")
    return df.set_index("soltu_id")

df = load_data()

# Web interface
st.title("Soltu to PGSC Converter")
st.write("Enter a Soltu gene ID to retrieve the corresponding PGSC ID and E-value.")

# Input
user_input = st.text_input("Soltu ID", "")

# Search
if user_input:
    if user_input in df.index:
        result = df.loc[user_input]
        st.success(f"**PGSC ID:** `{result['pgsc_id']}`\n\n**E-value:** `{result['evalue']}`")
    else:
        st.error("Soltu ID not found in the dataset.")

# Footer / Créditos
st.markdown("---")
st.markdown(
    "🧬 Developed by **Juan Ignacio Cortelezzi** at the "
    "[Plant Genetic Engineering Laboratory (INGEBI, CONICET)](https://ingebi-conicet.gov.ar/es_ingenieria-genetica-de-plantas/).",
    unsafe_allow_html=True
)
