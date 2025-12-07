from dotenv import load_dotenv
# import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import SystemMessage, HumanMessage,AIMessage
from langchain_core.prompts import PromptTemplate, load_prompt,ChatPromptTemplate

load_dotenv()
model = ChatGoogleGenerativeAI(
    model="gemini-pro-latest",  # OR: "gemini-1.5-flash", "gemini-1.5-pro"
)
chat_template=ChatPromptTemplate([
    SystemMessage(content="You are an expert in {domain}"),
    HumanMessage(content="Explain about {topic} in {this} way")
])
prompt=chat_template.invoke({"domain":"AI/ML","topic":"Transformers","this":"Technical"})
print(prompt)

# here the above code will not work as ChatPromptTemplate() behaves differently than the PromptTemplate()

from dotenv import load_dotenv
# import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import SystemMessage, HumanMessage,AIMessage
from langchain_core.prompts import PromptTemplate, load_prompt,ChatPromptTemplate

load_dotenv()
model = ChatGoogleGenerativeAI(
    model="gemini-pro-latest",  # OR: "gemini-1.5-flash", "gemini-1.5-pro"
)
chat_template=ChatPromptTemplate([
    ("system","You are an expert in {domain}"),
    ("human","Explain about {topic} in {this} way")
])
prompt=chat_template.invoke({"domain":"AI/ML","topic":"Transformers","this":"Technical"})
print(prompt)
