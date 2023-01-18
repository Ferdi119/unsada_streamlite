import streamlit as st

st.checkbox('yes')
st.button('Click')
st.radio('Pick your gender',['Male','Female','Classified'])
st.selectbox('Pick your gender',['Male', 'Female', 'Classified'])
st.multiselect('choose a planet',['Jupiter', 'Mars', 'neptune'])
st.select_slider('Pick a mark', ['Bad', 'Not Bad', 'Good', 'Very Good' ,'Excellent'])
st.slider('Pick a number', 0,50)