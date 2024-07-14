import streamlit as st

st.set_page_config(page_title="Home", page_icon="🏠")

st.title("Welcome to Dataset Manager")

st.markdown(
    """
    This is the home page of our Dataset Manager application.
    Use the sidebar to navigate to different pages:
    
    - **Datasets**: View existing datasets and create new ones
    - **Create Dataset**: Upload a new dataset
    """
)