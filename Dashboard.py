import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import time

# Setting page configuration
st.set_page_config(
    layout="wide",
    page_title="Property Dashboard",
    initial_sidebar_state="expanded"
)

@st.cache_data
def load_data():
    url = "E:\\jabodetabek_house_price.csv"  # Ganti dengan URL file CSV Anda
    data = pd.read_csv(url)  # Ganti dengan nama file CSV Anda
    return data

property_data = load_data()

group_members = {
    "Anggota Kelompok": [
        "Asgarindo Dwiki I.A.",
        "Aldien Maulana",
        "Aurelia Catherine L",
        "Monicha Ailsa Neha U",
    ]
}

st.sidebar.json(group_members)
st.sidebar.info("Team Members Loaded")
st.title("Jabodetabek Property Dashboard")
st.subheader("Welcome to the Big Data Property Dashboard!")
st.write("")
st.write("")


with st.sidebar:
        with st.spinner("Searching for data..."):
            time.sleep(2)
            st.write("Found URL.")
            time.sleep(1)
            st.write("Downloading data...")
            time.sleep(1)

st.sidebar.success("Data loaded successfully!")

# Visualizations
st.write("### Price Distribution")
if 'price_in_rp' in property_data.columns:
    # Attempt to convert 'price_in_rp' to numeric, coercing errors to NaN
    property_data['price_in_rp'] = pd.to_numeric(property_data['price_in_rp'], errors='coerce')
    
    # Remove rows with NaN values in 'price_in_rp'
    property_data = property_data.dropna(subset=['price_in_rp'])
    
    # Plot area chart
    st.area_chart(property_data['price_in_rp'])
else:
    st.write("Price_in_rp column not found in the dataset.")


# Visualizations
st.write("### Property Type Distribution")
if 'property_type' in property_data.columns:
    property_type_counts = property_data['property_type'].value_counts()
    property_type_table = pd.DataFrame({'Property Type': property_type_counts.index, 'Count': property_type_counts.values})

    st.table(property_type_table)
else:
    st.write("Property_Type column not found in the dataset.")


