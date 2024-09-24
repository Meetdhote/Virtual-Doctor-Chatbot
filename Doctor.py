import os
import openai
import streamlit as st
from dotenv import load_dotenv 

load_dotenv()

openai.api_type = "azure"
openai.api_version = os.getenv("AZURE_OPENAI_API_VERSION","").strip()

API_KEY = os.getenv("AZURE_OPENAI_API_KEY","").strip()
assert API_KEY, "ERROR: Azure OpenAI Key is missing"
openai.api_key = API_KEY

RESOURCE_ENDPOINT = os.getenv("OPENAI_API_BASE","").strip()
assert RESOURCE_ENDPOINT, "ERROR: Azure OpenAI Endpoint is missing"
assert "openai.azure.com" in RESOURCE_ENDPOINT.lower(), "ERROR: Azure OpenAI Endpoint should be in the form: \n\n\t<your unique endpoint identifier>.openai.azure.com"
openai.api_base = RESOURCE_ENDPOINT


deployment = "TG-OAi-GPTModel"


def get_response(user_input):
    text_prompt = user_input
    response = openai.ChatCompletion.create(
        engine=deployment,
        messages=[
            {"role": "system", "content": "I'm a doctor, specialist on surgery"},
            {"role": "user", "content": text_prompt},
        ]
    )
    return response['choices'][0]['message']['content']

# Set up Streamlit app
st.title("Virtual Doctor Chatbot")
st.write("Ask any medical question and get a response from the AI doctor.")

# User input
user_input = st.text_input("Your Question:", "")

if st.button("Get Response"):
    if user_input:
        response = get_response(user_input)
        st.write("**Doctor's Response:**")
        st.write(response)
    else:
        st.warning("Please enter a question.")
