import streamlit as st
import pandas as pd
import time
from dataProcessing import process_data

# Load property data
@st.cache_data
def load_data():
    try:
        # Load and clean data from dataProcessing.py
        cleaned_data = process_data()

        # Convert Spark DataFrame to Pandas DataFrame
        cleaned_data_pandas = cleaned_data.toPandas()

        return cleaned_data_pandas
    except Exception as e:
        st.error(f"Error loading data: {e}")
        return None

# Set page configuration
st.set_page_config(
    layout="wide",
    page_title="Property Dashboard",
    initial_sidebar_state="expanded"
)

# Load property data
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

# Display location map
st.subheader('Property Locations')
if property_data is not None:
    if 'lat' in property_data.columns and 'long' in property_data.columns:
        # Rename 'long' column to 'lon' for Streamlit compatibility
        map_data = property_data.rename(columns={'long': 'lon'})[['lat', 'lon']].dropna()

        # Convert 'lat' and 'lon' columns to float
        map_data['lat'] = map_data['lat'].astype(float)
        map_data['lon'] = map_data['lon'].astype(float)

        st.map(map_data)
    else:
        st.write("Latitude or Longitude columns not found in the dataset.")
else:
    st.error("Failed to load data. Please check the file path and try again.")
