import streamlit as st
import os
import google.generativeai as genai
from PIL import Image

from dotenv import load_dotenv
load_dotenv()

genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

def get_gemini_response_for_invoice(sys_message, image, input):
    model = genai.GenerativeModel('gemini-pro-vision')
    response = model.generate_content([sys_message, image, input])
    return response.text

st.set_page_config(page_title='Invoice Bot')
st.header('Gemini Invoice Application')

input = st.text_input("Input: ", key='input')
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
image=""   
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image.", use_column_width=True)
button = st.button("Submit")

sys_message = """
               You are an expert in understanding invoices.
               You will receive input images as invoices &
               you will have to answer questions based on the input image
               """

if button:
    response = get_gemini_response_for_invoice(sys_message, image, input)
    st.subheader("Response: ")
    st.write(response)