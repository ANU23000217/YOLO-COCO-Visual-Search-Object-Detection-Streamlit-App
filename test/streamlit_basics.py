
import streamlit as st

# basics element
st.title("Streamlit Intro")
st.write("This is where we'll learn streamlit")

# Getting user input
name = st.text_input("What's your name?")
if name:
    st.write(f"Welcome, {name}! Ready to build something amazing?")