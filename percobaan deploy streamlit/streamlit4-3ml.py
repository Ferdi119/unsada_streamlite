import streamlit as st
import time

st.balloons()

st.subheader("please waiting")
st.progress(50)

st.subheader("Still Loading")
with st.spinner('Wait for it...'):
 time.sleep(100)
