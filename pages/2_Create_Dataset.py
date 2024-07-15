import streamlit as st
import pandas as pd
import os
from supabase import create_client, Client
from supabase.lib.client_options import ClientOptions
from df_functions import get_file_details
import time 

st.set_page_config(page_title="Create Dataset", page_icon="➕")

@st.cache_resource
def init_connection():
    url = st.secrets["supabase"]["url"]
    key = st.secrets["supabase"]["key"]
    opts = ClientOptions().replace(schema="personal_ml")
    return create_client(url, key, options=opts)

supabase = init_connection()

st.title("Create Dataset")

uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
df = None
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    
    st.write("Preview of the uploaded CSV:")
    st.write(df.head())

    columns = df.columns.tolist()
    data_types = df.dtypes.astype(str).tolist()
    
    target_col = st.selectbox("Select the Target column", columns)
 
    if st.button(label = "get details"):
        if df is None:
            st.error('Please upload the df first')
        else:
            st.write("Columns and Data Types:")
            basic_details, column_info = get_file_details(df, target_col)
            st.write("Number of Rows:", basic_details['Rows'], "Number of Columns:", basic_details['Columns'])
            st.write(column_info)

    if st.button(label="submit"):
        table_name = "datasets"
        data = {
            "created_by": "Srujeeth",
            "status": "Pending"
        }
        
        response = supabase.table("datasets").insert(data).execute()
        max_id = supabase.table("datasets").select("id").order('id', desc=True).limit(1).execute().data[0]['id']

        save_path = f"uploads/{max_id}.csv"
        if not os.path.exists('uploads/'):
            os.makedirs('uploads/')
        
        file_path = os.path.join(save_path)
        df.to_csv(file_path, index=False)
        
        time.sleep(5)

if st.button("Back to Datasets"):
    st.switch_page("pages/1_Datasets.py")