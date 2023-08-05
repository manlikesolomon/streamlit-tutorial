import streamlit as st
import numpy as np
import pandas as pd
import altair as alt

# add our header
st.write('st.write')

# practice 1
st.write('Hello *World!* :sunglasses:')

# practice 2
st.write(1234)

# practice 3
df = pd.DataFrame({
    'first column': [1,2,3,4],
    'second column': [10,20,30,40]})

if st.checkbox('Click to see df'):
    st.write(df)

#practice 4
st.write('Above dataframe', df, 'Below dataframe')

#practice 5
df2 = pd.DataFrame(
    np.random.randn(200,3),
    columns=['a','b','c'])

chart = alt.Chart(df2).mark_circle().encode(x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])

st.write(chart)