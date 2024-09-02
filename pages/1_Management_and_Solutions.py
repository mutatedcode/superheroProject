import streamlit as st
import pandas as pd


page_bg_img = """
<style>
[data-testid="stAppViewContainer"] {
background: rgb(219,213,246);
background: linear-gradient(0deg, rgba(219,213,246,1) 0%, rgba(21,71,146,1) 100%);
}
</style>
"""


st.markdown(page_bg_img, unsafe_allow_html=True)
st.markdown("<h1 style='text-align: center'>Management and Solutions</h2>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center'>Registered Power Persons Entity Dataset</h2>", unsafe_allow_html=True)

st.divider()

st.markdown("<p style='text-align: center'> To ensure safety among all citizens of Earth and nearby systems, HeroTech Innovations takes pride in having a publicly available dataset for all registered powered persons.</h2>", unsafe_allow_html=True)

data = pd.read_csv(r"C:\Users\layla\OneDrive\Documents\GitHub\superheroProject\superheroes_nlp_dataset.csv")
st.write(data)