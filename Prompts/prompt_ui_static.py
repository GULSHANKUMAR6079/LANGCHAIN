from dotenv import load_dotenv
import streamlit as st

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate, load_prompt

load_dotenv()

# Gemini Chat Model (choose gemini-1.5-pro or flash)
model = ChatGoogleGenerativeAI(
    model="gemini-pro-latest",  # OR: "gemini-1.5-flash", "gemini-1.5-pro"
    temperature=0.3
)

st.header('Research Tool')

user_input=st.text_input("ENTER YOUR PROMPT")
if st.button("SUMMARIZE"):
    result=model.invoke(user_input)
    st.write(result.content)