import streamlit as st
import time

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


def about_page():
    st.title("About This App")
    
    st.markdown("""
    This application is created to provide big data visualization and exploration features for property data. It allows users to analyze various aspects of property data, apply filters to refine their analysis, and visualize insights through interactive charts and tables.

    ### Features:
    - **Raw Data Exploration:** Explore the raw property data including details such as price, location, facilities, and more.
    - **Filters:** Filter the data based on city, district, price range, and other criteria to focus on specific segments.
    - **Data Visualization:** Visualize the filtered data using interactive charts like histograms, scatter plots, and bar charts.
    
    ### Data Source:
    The property data used in this application is sourced from [Jabodetabek House Price Dataset](https://www.kaggle.com/datasets/nafisbarizki/daftar-harga-rumah-jabodetabek?resource=download).

    ### Team Members:
    - **Asgarindo Dwiki Ibrahim Adji**
    - **Aldien Maulana**
    - **Aurelia Catherine Lay**
    - **Monicha Ailsa Neha Utomo** 

    ### Contact Us:
    For any inquiries or feedback, feel free to reach out to us at [team@example.com](mailto:team@example.com).
    """)

if __name__ == "__main__":
    about_page()
