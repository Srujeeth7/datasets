import streamlit as st
import pandas as pd
from supabase import create_client, Client
import os
from supabase.lib.client_options import ClientOptions

st.set_page_config(page_title="Dataset Details", page_icon="🔍")

@st.cache_resource
def init_connection():
    url = st.secrets["supabase"]["url"]
    key = st.secrets["supabase"]["key"]
    opts = ClientOptions().replace(schema="personal_ml")
    return create_client(url, key, options=opts)

supabase = init_connection()

if 'id' in st.query_params:
    dataset_id = st.query_params.id
    
    response = supabase.table("datasets").select("*").eq('id', dataset_id).execute()
    dataset = response.data[0] if response.data else None
    st.dataframe(dataset)
    
    if dataset:
        st.write(f"**ID:** {dataset['id']}")        

        if st.button("View Data"):
            try:
                df = pd.read_csv(f'uploads/{dataset["id"]}.csv')
                st.dataframe(df)
            except FileNotFoundError:
                st.error("File not found. It may have been moved or deleted.")
    else:
        st.error("Dataset not found.")
else:
    st.error("No dataset selected. Please go back to the Datasets page and select a dataset.")

if st.button("Back to Datasets"):
    st.switch_page("pages/1_Datasets.py")