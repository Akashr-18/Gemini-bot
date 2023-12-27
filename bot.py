import streamlit as st
import os
import google.generativeai as genai

from dotenv import load_dotenv
load_dotenv()

genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

def get_gemini_response(question):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(question)
    return response.text

st.set_page_config(page_title='Q&A demo')
st.header("Gemini Text Bot")

input = st.text_input("Input: ", key='input')
button = st.button('Submit')

if input and button:
    response = get_gemini_response(input)
    st.subheader("Response: ")
    st.write(response)