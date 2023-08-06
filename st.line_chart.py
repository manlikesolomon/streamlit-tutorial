import pandas as pd
import numpy as np
import streamlit as st

st.header('st.line_chart \U0001F4CC')

# create random chart data and store in a dataframe
chart_data = pd.DataFrame(data=np.random.randn(20,3),
                          columns=('Feature1', 'Feature2', 'Feature3'))

st.line_chart(chart_data)