import streamlit as st
from datetime import datetime
from langchain.prompts import PromptTemplate

today = datetime.today().strftime("%H:%M:%S")


st.title("ga11o!")

st.write(today)

select_model = st.selectbox("select model!", ("llama2", "mistral"))

st.write(select_model)

if select_model == "llama2":
    st.write("this is llama2:7b!")
else:
    st.write("this is mistral latest!")

        
    name = st.text_input("input your name!")

    st.write(name)

    value = st.slider("temp", min_value=0.1, max_value=0.9)
    st.write(value)