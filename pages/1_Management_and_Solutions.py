import os
import streamlit as st
import pandas as pd
from pandasai import SmartDataframe
from pandasai.llm import OpenAI
from ai import get_api_key

# Get API key from environment or another source
api_key = get_api_key()

# Page background and style
page_bg_img = """
<style>
[data-testid="stAppViewContainer"] {
background: rgb(219,213,246);
background: linear-gradient(0deg, rgba(219,213,246,1) 0%, rgba(21,71,146,1) 100%);
}
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)

# Title and description
st.markdown("<h1 style='text-align: center'>Management and Solutions</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center'>Registered Powered Persons Dataset</h3>", unsafe_allow_html=True)
st.divider()
st.markdown("<p style='text-align: center'>To ensure safety among all citizens of Earth and nearby systems, HeroTech Innovations takes pride in having a publicly available dataset for all registered powered persons.</p>", unsafe_allow_html=True)

# Load the data
data = pd.read_csv("https://raw.githubusercontent.com/mutatedcode/superheroProject/main/superheroes_nlp_dataset.csv")

# Display the data
with st.expander("Registered Powered Persons Library"):
    st.write(data)

# Query input
query = st.text_area("Ask more about Superpowered Persons")
if query:
    # Ensure the OpenAI API key is loaded from environment variables
    os.environ["OPENAI_API_KEY"] = api_key
    
    # Initialize the OpenAI LLM and SmartDataframe with the data
    llm = OpenAI(api_token=api_key)
    smart_df = SmartDataframe(data, config={"llm": llm})
    
    try:
        # Perform the query and display the answer
        answer = smart_df.chat(query)
        
        # Display the answer based on its type
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
