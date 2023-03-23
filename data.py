import streamlit as st
from sqlalchemy import create_engine, text
import pandas as pd
from PIL import Image

st.title('Добро пожаловать на сервер шизофрения')
user_input = st.text_input("Enter URL of your DB:")
st.write('Example: sqlite:///sqlite-sakila.db')
if "user_input" not in st.session_state:
    st.session_state.user_input = ''
add_button = st.button("Add")
if add_button:
    st.session_state.user_input = user_input
if len(user_input) == 0:
    engine = create_engine('sqlite:///sqlite-sakila.db')
else:
    engine = create_engine(st.session_state.user_input)

query = "SELECT name FROM sqlite_master WHERE type='table'"
df = pd.read_sql(text(query), engine.connect())
st.write('Таблицы, которые содержатся в базе данных:')
st.write(df)

user_query = st.text_input("Enter SQL query:")
try:
    df_query = pd.read_sql(text(user_query), engine.connect())
    st.write('Output:')
    st.write(df_query)
except Exception as e:
    st.write('Error null or wrong query!')
    st.write('NOTE: The app uses sqlite')


