import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import time

# Load property data
@st.cache_data
def load_data():
    # Load your property data here
    # Replace 'path_to_your_csv_file' with the actual path to your CSV file
    property_data = pd.read_csv("E:\\jabodetabek_house_price.csv")
    return property_data

# Set page configuration
st.set_page_config(layout="wide",
    page_title="Property Dashboard",
    initial_sidebar_state="expanded")

# Load property data
property_data = load_data()

group_members = {
    "Anggota Kelompok": [
        "Asgarindo Dwiki I.A.",
        "Aldien Maulana",
        "Hafidz Fathurrohman",
        "Muhammad Fikri",
    ]
}

st.sidebar.json(group_members)
with st.sidebar.status("Downloading data..."):
    st.write("Searching Location...")
    time.sleep(2)
    st.write("Found Location.")
    time.sleep(1)

st.sidebar.success("Data loaded successfully!")

# Display location map
st.subheader('Property Locations')
if 'lat' in property_data.columns and 'long' in property_data.columns:
    # Rename 'long' column to 'lon' for Streamlit compatibility
    map_data = property_data.rename(columns={'long': 'lon'})[['lat', 'lon']].dropna()
    st.map(map_data)
else:
    st.write("Latitude or Longitude columns not found in the dataset.")
