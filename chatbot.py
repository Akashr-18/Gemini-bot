import streamlit as st
import os
import google.generativeai as genai

from dotenv import load_dotenv
load_dotenv()

genai.configure(api_key = os.getenv('GOOGLE_API_KEY'))


model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])
resp = chat.send_message("Who is ms dhoni? Write a short note on him in less than 50 words")
respo = resp.text

def get_gemini_response(input):    
    response = chat.send_message(input)
    return response.text

st.set_page_config(page_title='Img Bot')
st.header('Gemini Chatbot')

if "chat_history" not in st.session_state:
    st.session_state['chat_history'] = []

input=st.text_input("Input: ",key="input")
submit=st.button("Ask the question")

if input and submit:
    response = get_gemini_response(input)
    st.session_state['chat_history'].append(("You",  input))
    st.subheader("The Response is")
    st.write(response)
    st.session_state['chat_history'].append(("Bot", response))
    st.subheader("Chat History: ")
    for message in chat.history:
        st.write(f'**{message.role}**: {message.parts[0].text}')
    st.write(chat.history)

# st.subheader("Chat History: ")

#Taking only current chat history
# for message in chat.history:
#     st.write(f'**{message.role}**: {message.parts[0].text}')

# Just storing chat history in session state and displaying all at once . That's all
# for role, text in st.session_state['chat_history']:
#     st.write(f"**{role}**: {text}")

# st.subheader("ZZZ")
# st.write(chat.history)