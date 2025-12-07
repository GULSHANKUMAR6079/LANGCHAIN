
from dotenv import load_dotenv
# import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import SystemMessage, HumanMessage,AIMessage
from langchain_core.prompts import PromptTemplate, load_prompt,ChatPromptTemplate, MessagesPlaceholder

load_dotenv()
#Chat_Template
chat_template=ChatPromptTemplate([
    ("system","You are a helpful and Intelligent Customer Support Agent"),
    MessagesPlaceholder(variable_name="chat_history"),
    ("human","{query}")
])
chat_history=[]
# load chat history
with open("Prompts\\chat_history.txt")as f:
    chat_history.extend(f.readlines())
print(chat_history)

# Create Prompt
prompt=chat_template.invoke({"chat_history":chat_history,"query":"Where is my refund"})
print(prompt)