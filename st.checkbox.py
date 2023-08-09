import streamlit as st

st.header('st.checkbox')

icecream = st.checkbox('Icecream')
coffee = st.checkbox('Coffee')
beer = st.checkbox('Beer')

if icecream:
    st.write('Have your ice cream :icecream:')

if coffee:
    st.write('Have your coffee :coffee:')

if beer:
    st.write('Have your beer :beer:')