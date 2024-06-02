import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import time

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

st.subheader('Property Data')
st.write('Explore the raw data of properties.')

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
    st.write("Searching for data...")
    time.sleep(2)
    st.write("Found URL.")
    time.sleep(1)
    st.write("Downloading data...")
    time.sleep(1)

st.sidebar.success("Data loaded successfully!")

# Pastikan data dimuat dengan benar
st.write("### Data Preview")
st.table(property_data.head())