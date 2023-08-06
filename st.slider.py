import streamlit as st
from datetime import time, datetime

# add our header
st.header(':blue[Streamlit Sliders]: st.slider')

# practice 1
st.subheader('Slider')

age = st.slider('Select your age on the slider', 0,100,26)
st.write(f'You are {age} years old')

# practice 2
values = st.slider('Select a range',
                   0.0, 100.0, (25.0,50.0))
st.write('Values:', values)

# practice 3
st.subheader('Time Slider')

app_time = st.slider('When did you start?',
                       value=(time(11,00),time(15,45)))

start_time = app_time[0].strftime("%H:%M")
end_time = app_time[1].strftime("%H:%M")

st.write(f'Your appointment time is {start_time} to {end_time}')

# practice 5 
st.subheader('Datetime Slider')

start_date = st.slider("When do you want to start",
                       value=datetime(2023, 1, 1,12,30),
                       format='MM/DD/YY - hh:mm')
st.write("Start date:", start_date)

