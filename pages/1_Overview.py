import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import time
import locale

# Caching data to improve performance
@st.cache_data
def load_data():
    try:
        # Load your property data here
        # Replace 'path_to_your_csv_file' with the actual path to your CSV file
        property_data = pd.read_csv("E:\\jabodetabek_house_price.csv")
        return property_data
    except Exception as e:
        st.error(f"Error loading data: {e}")
        return None

# Set page configuration
st.set_page_config(
    layout="wide",
    page_title="Property Dashboard",
    initial_sidebar_state="expanded"
)

# Subheader and raw data exploration
st.subheader('Property Data')
st.write('Explore the raw data of properties.')

property_data = load_data()

if property_data is not None:
    # Display group members in the sidebar
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

    # Sidebar for data loading status
    with st.sidebar:
        with st.spinner("Searching for data..."):
            time.sleep(2)
            st.write("Found URL.")
            time.sleep(1)
            st.write("Downloading data...")
            time.sleep(1)

    st.sidebar.success("Data loaded successfully!")

    # Add a checkbox for showing raw data
    if st.checkbox('Show Raw Data'):
        st.write("### Full Data")
        st.dataframe(property_data)

    # Adding filters
    st.subheader("Filters")

    # Filter by city
    if 'city' in property_data.columns:
        cities = property_data['city'].unique()
        selected_cities = st.multiselect("Select City", cities, default=[])
    else:
        st.error("'city' column not found in data.")
        selected_cities = []

    # Filter by district
    if 'district' in property_data.columns:
        districts = property_data['district'].unique()
        selected_districts = st.multiselect("Select District", districts, default=[])
    else:
        st.error("'district' column not found in data.")
        selected_districts = []

    # Filter by price range
    if 'price_in_rp' in property_data.columns:
        min_price = int(property_data['price_in_rp'].min())
        max_price = int(property_data['price_in_rp'].max())
        min_price_idr = locale.format_string("%d", min_price, grouping=True)
        max_price_idr = locale.format_string("%d", max_price, grouping=True)
        selected_price = st.slider("Select Price Range (IDR)", min_price, max_price, (min_price, max_price), format="IDR %d")
    else:
        st.error("'price_in_rp' column not found in data.")
        selected_price = (0, 0)


    # Apply filters to data
    filtered_data = property_data

    if selected_cities:
        filtered_data = filtered_data[filtered_data['city'].isin(selected_cities)]

    if selected_districts:
        filtered_data = filtered_data[filtered_data['district'].isin(selected_districts)]

    if selected_price != (0, 0):
        filtered_data = filtered_data[
            (filtered_data['price_in_rp'] >= selected_price[0]) &
            (filtered_data['price_in_rp'] <= selected_price[1])
        ]

    # Display filtered data preview
    st.write("### Filtered Data")
    st.dataframe(filtered_data)

else:
    st.error("Failed to load data. Please check the file path and try again.")
