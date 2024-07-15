import streamlit as st
import pandas as pd
from supabase import create_client, Client
from supabase.lib.client_options import ClientOptions

st.set_page_config(page_title="Datasets", page_icon="📊")



@st.cache_resource
def init_connection():
    url = st.secrets["supabase"]["url"]
    key = st.secrets["supabase"]["key"]
    opts = ClientOptions().replace(schema="personal_ml")
    return create_client(url, key, options=opts)

supabase = init_connection()


@st.cache_resource 
def fetch_dataset_details_from_db():
    response = supabase.table("datasets").select("*").execute()
    return response.data

def generate_url(row_id):
    return f"http://localhost:8501/Dataset_Details?id={row_id}"

def highlight_rows(row):
    if row['status'] == 'SUCCESS':
        return ['background-color: lightgreen'] * len(row)
    elif row['status'] == 'Pending':
        return ['background-color: lightyellow'] * len(row)
    elif row['status'] == 'Error':
        return ['background-color: lightcoral'] * len(row)
    else:
        return [''] * len(row)

st.title("Datasets")

col1, col2, col3 = st.columns([1, 4, 1])

with col1:
    if st.button("Create Dataset"):
        st.switch_page("pages/2_Create_Dataset.py")

datasets = fetch_dataset_details_from_db()
with col3:
    if st.button("Refresh Data"):
        datasets = fetch_dataset_details_from_db()
if datasets:
    df = pd.DataFrame(datasets)
    df["View Details"] = df['id'].apply(lambda x: f"<a target='_blank' href='{generate_url(x)}'>View Details</a>")
    
    styled_page_df = df.style.apply(highlight_rows, axis=1).set_properties(subset=['View Details'], **{'text-align': 'left'})
    st.write(styled_page_df.to_html(escape=False), unsafe_allow_html=True)
else:
    st.info("No datasets available. Create a new dataset to get started!")