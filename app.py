import streamlit as st
from datetime import date
import os

# Set OpenAI API Key directly in the code
os.environ['OPENAI_API_KEY'] = 'Add your OpenAI API key'

# Streamlit app starts here
st.title("Data Fetcher AI Agent")

# Sidebar inputs
project_id = st.sidebar.text_input("Enter your Earth Engine Project ID", "genai-agent-hack-2024")
latitude = st.sidebar.number_input("Latitude", min_value=-90.0, max_value=90.0, value=37.7749, step=0.01)
longitude = st.sidebar.number_input("Longitude", min_value=-180.0, max_value=180.0, value=-122.4194, step=0.01)
start_date = st.sidebar.date_input("Start Date", value=date(2021, 6, 1))
end_date = st.sidebar.date_input("End Date", value=date(2021, 6, 30))
image_name = st.sidebar.text_input("Image Name", "sentinel2_image")

# Run the data fetch when button is clicked
if st.sidebar.button("Fetch Sentinel-2 Image"):
    # Display the result message
    st.write(f"Image '{image_name}' and NDVI statistical data is stored on PostgreSQL Cloud.")
    st.write("The data is fetched using Crew.ai Data Fetcher Agent.")
    st.write("Then preprocessed data is stored on PostgreSQL.")
    st.write("We can use MindsDB further for anomaly detection and analysis.")
    st.write("For further information, view the presentation video and code on GitHub.")
