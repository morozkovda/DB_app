import streamlit as st
from sqlalchemy import create_engine, text
import pandas as pd
import webbrowser
from PIL import Image

def open_youtube():
    webbrowser.open('https://www.youtube.com/watch?v=dQw4w9WgXcQ')

st.title('Welcome to simple DB app!')
user_input = st.text_input("Enter URL of your DB:")
st.write('Example: sqlite:///sqlite-sakila.db')
if "user_input" not in st.session_state:
    st.session_state.user_input = ''
if st.button('Add'):
    open_youtube()


