import streamlit as st

st.title('Customizing the theme for streamlit')

st.write('Content of the `.streamlit/config.toml` file for this app')

st.code("""
        [theme]
        primaryColor="#F39C12"
        backgroudColor="#2E86C1"
        secondaryBackgroundColor="#AED6F1"
        textColor="#FFFFFF"
        font="monospace"
        """)