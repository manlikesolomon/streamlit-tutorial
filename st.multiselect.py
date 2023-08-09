import streamlit as st

st.header('st.multiselect :slot_machine:')

colors = st.multiselect('Select from the options',
               ['red','yellow','blue','green','orange'])

st.write('You selected', colors)

