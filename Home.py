import streamlit as st
import pandas as pd
import math


page_bg_img = """
<style>
[data-testid="stAppViewContainer"] {
background: rgb(219,213,246);
background: linear-gradient(0deg, rgba(219,213,246,1) 0%, rgba(21,71,146,1) 100%);
}
</style>
"""


st.markdown(page_bg_img, unsafe_allow_html=True)
st.markdown("<h1 style='text-align: center'> Welcome to HeroTech Innovations</h1>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center'>Pioneering a Safer Future</h2>", unsafe_allow_html=True)

st.divider()

container = st.container(border=True)
container.image("https://screenrant.com/wp-content/uploads/2016/10/Supergirl-In-Flight.jpg")
st.caption("<p style='text-align: center'> Supergirl, whose navigation technologies are powered by HeroTech. Learn more about our products below. </h1>", unsafe_allow_html=True)

st.divider()

st.markdown("<h1 style='text-align: center'> Our Mission </h1>", unsafe_allow_html=True)

st.markdown("<h3 style='text-align: center'> Since 2118, we, at HeroTech Innovations, are devoted to making the world a greater and safer place for all of Earth and its surrounding systems. </h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center'> Creating software that our amazing heroes can utilize, so they can continue saving the world. </h1>", unsafe_allow_html=True)


st.divider()

st.markdown("<h1 style='text-align: center'> Our Products </h1>", unsafe_allow_html=True)

st.divider()

