import os
import dotenv
import streamlit as st
from main import get_summary

# Retrieve the OpenAI API key from the environment variable
dotenv.load_dotenv()
openai_api_key = os.environ.get("OPENAI_API_KEY")

# Declare the model to use. 
model = 'gpt-3.5-turbo-16k'
# model = 'gpt-3.5-turbo'

# Set the page color to green
st.set_page_config(
    page_title='PDF Summarizer',
    page_icon='✒️',
    layout='wide',
    initial_sidebar_state='collapsed',
)

# Setting Up The Application Landing Page
st.markdown("""
# PDF Document Summarizer

###### This is a simple web application that uses OpenAI's GPT-3.5 Turbo model to generate a summary of a PDF document. 
###### To get started, please enter your OpenAI API Key and upload a PDF file.
###### When ready click the "Submit" button to generate your summary. 
""")

def generate_response(doc, model, openai_api_key):
    # Use st.spinner to show a loading spinner while the model is working
    with st.spinner("Generating summary..."):
        output = get_summary(doc, model, openai_api_key)
        st.write(output)

with st.form('my_form'):
    if openai_api_key is None:
        openai_api_key = st.text_input('OpenAI API Key', 'Enter Your OpenAI API Key', type='password')

    files = st.file_uploader("Upload files", type=["pdf"], accept_multiple_files=False)

    submitted = st.form_submit_button('Submit')

    if submitted:
        generate_response(files, model, openai_api_key)
