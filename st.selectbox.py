import streamlit as st

st.header('st.selectbox')

color = st.selectbox("Pick a color :studio_microphone:", ('Red','Blue','Yellow'))

st.write('Your color is',color)