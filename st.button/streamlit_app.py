import streamlit as st

st.header('st.button')


if st.button(':blue[Say hello]'):
    st.write('Hello who is there!')
else:
    st.write('Goodbye')