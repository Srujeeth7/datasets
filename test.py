# import pandas as pd
# import streamlit as st
# from st_material_table import st_material_table

# df = pd.read_csv("https://storage.googleapis.com/tf-datasets/titanic/train.csv")

# _ = st_material_table(df)

import streamlit as st

tab1, tab2, tab3 = st.tabs(["Cat", "Dog", "Owl"])

with tab1:
   st.header("A cat")
   st.image("https://static.streamlit.io/examples/cat.jpg", width=200)

with tab2:
   st.header("A dog")
   st.image("https://static.streamlit.io/examples/dog.jpg", width=200)

with tab3:
   st.header("An owl")
   st.image("https://static.streamlit.io/examples/owl.jpg", width=200)
