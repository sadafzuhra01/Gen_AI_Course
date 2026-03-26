import streamlit as st
import pandas as pd


## Title 
st.write(
    """
    ## This is my first project
    This is a simple project to get started with Streamlit.
"""
)

name = st.text_input("Write your name here:")

st.write(f" Hello, {name}! ")


data = pd.DataFrame({
    "Feature 1" : [1,2,3,4,5,6,7,7],
    "Feature 2" : [2,3,1,5,6,7,8,9],
    "Feature 3" : [3,4,5,6,7,8,3,1]
})

st.write(data)

st.write("This is the end of my application.")

