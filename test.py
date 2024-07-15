import pandas as pd
import streamlit as st
from st_material_table import st_material_table

df = pd.read_csv("https://storage.googleapis.com/tf-datasets/titanic/train.csv")

_ = st_material_table(df)
