import streamlit as st
import pandas as pd
import plotly.express as px

st.title('st.file_uploader')

# write a subheader
st.subheader('Input csv')

# upload a file and store in a variable
uploaded_file = st.file_uploader(label='Choose a file')

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.subheader('Dataframe')
    st.write(df.head())
    st.subheader('Descriptive Statistics')
    st.write(df.describe())
    last_column = df.columns[-1]
    fig = px.histogram(df, last_column,nbins=10)
    fig.update_layout(title_text=f"Distrubution of {last_column}")
    st.subheader('Distribution of Target Variable')
    st.plotly_chart(fig)
else:
    st.info(':coffee: Upload a csv file.')

