import streamlit as st
import os
import google.generativeai as genai
from PIL import Image

from dotenv import load_dotenv
load_dotenv()

genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

def gemini_blog_creation(image, input):
    model = genai.GenerativeModel('gemini-pro')
    model_vision = genai.GenerativeModel('gemini-pro-vision')
    if (input != "") and (image == ""):
        print("Loop1")
        system_message = """
               As a blog post content creator, you will be receiving topic name in the text format. 
               Your task is to generate a well-structured and engaging English language blog post centered around that topic. 
               To ensure clarity and organization, please include several subtopics within the main topic, each with their own distinct section or heading. 
               Write in a conversational yet informative tone, aiming to provide value and insights to readers while keeping them engaged throughout the post.
               """
        response = model.generate_content([system_message, input])
    elif (input == "") and (image != ""):
        print("Loop2")
        system_message = """
               You will receive input as image. Describe the image in one sentence.
               As a blog post content creator, your task is to generate a well-structured and engaging blog post centered around that topic. 
               Blog post content should be written in standard American English format.
               To ensure clarity and organization, please include several subtopics within the main topic, each with their own distinct section or heading. 
               Write in a conversational yet informative tone, aiming to provide value and insights to readers while keeping them engaged throughout the post.
               """
        response = model_vision.generate_content([system_message, image])
    elif (input != "") and (image != ""):
        print("Loop3")
        system_message = """
               You are content creator for blog post.
               You will receive input as both image and text.
               Your task is to generate a new blog post content based on the text and image provided for you. If the text and image are not related then return the response as "No Response".
               """
        response = model_vision.generate_content([system_message, image, input], stream=True)
    else:
        response = ""
    return response

st.set_page_config("Blog Post Generator")
st.header("Blog Post  Generator")

input = st.text_input("Enter the topic", key='input')
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
image=""   
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image.", use_column_width=True)
button = st.button("Get Blog content")

if button:
    response = gemini_blog_creation(image, input)
    st.subheader("Response: ")
    # for chunk in response:
    #     st.write(chunk.text)
    st.write(response.text)



