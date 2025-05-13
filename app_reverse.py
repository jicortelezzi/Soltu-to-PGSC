# app_reverse.py
import pandas as pd
import streamlit as st

# Load data
@st.cache_data
def load_data():
    df = pd.read_csv("resultado_sequencias.csv")
    return df.set_index("pgsc_id")

df = load_data()

# Web interface
st.title("PGSC to Soltu Converter")
st.write("Enter a PGSC gene ID to retrieve the corresponding Soltu ID and E-value.")

# Input
user_input = st.text_input("PGSC ID", "")

# Search
if user_input:
    if user_input in df.index:
        result = df.loc[user_input]
        st.success(f"**Soltu ID:** `{result['soltu_id']}`\n\n**E-value:** `{result['evalue']}`")
    else:
        st.error("PGSC ID not found in the dataset.")

# Credits
st.markdown("---")
st.markdown(
    "🧬 Developed by **Juan Ignacio Cortelezzi** at the "
    "[Plant Genetic Engineering Laboratory (INGEBI, CONICET)](https://ingebi-conicet.gov.ar/es_ingenieria-genetica-de-plantas/).",
    unsafe_allow_html=True
)