import os
import streamlit as st
import pandas as pd
from pandasai import SmartDataframe
from pandasai.llm import OpenAI

page_bg_img = """
<style>
[data-testid="stAppViewContainer"] {
background: rgb(219,213,246);
background: linear-gradient(0deg, rgba(219,213,246,1) 0%, rgba(21,71,146,1) 100%);
}
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center'>Management and Solutions</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center'>Registered Powered Persons Dataset</h3>", unsafe_allow_html=True)
st.divider()
st.markdown("<p style='text-align: center'>To ensure safety among all citizens of Earth and nearby systems, HeroTech Innovations takes pride in having a publicly available dataset for all registered powered persons.</p>", unsafe_allow_html=True)

data = pd.read_csv("https://raw.githubusercontent.com/mutatedcode/superheroProject/main/superheroes_nlp_dataset.csv")

with st.expander("Registered Powered Persons Library"):
    st.write(data)

query = st.text_area("Ask more about Superpowered Persons")
if query:
    os.environ['OPENAI_API_KEY'] = st.secrets['api_key']
    
    llm = OpenAI(api_token=st.secrets['api_key'])
    smart_df = SmartDataframe(data, config={"llm": llm})
    
    try:

        answer = smart_df.chat(query)
        
        if isinstance(answer, pd.DataFrame):
            st.write("Answer is a DataFrame:")
            st.write(answer)
        elif isinstance(answer, str):
            st.write("Answer is a text response:")
            st.write(answer)
        else:
            st.write(f"Answer is of unexpected type: {type(answer)}")
            st.write(answer)
    
    except Exception as e:
        st.error(f"An error occurred: {e}")
