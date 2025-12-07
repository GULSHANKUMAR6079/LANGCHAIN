#  # pyright: ignore[reportMissingImports]
from langchain_core.messages import SystemMessage, HumanMessage,AIMessage
from langchain_google_genai import ChatGoogleGenerativeAI
# from dotenv import load_dotenv
# load_dotenv()
# model = ChatGoogleGenerativeAI(
#     model="gemini-pro-latest",  # OR: "gemini-1.5-flash", "gemini-1.5-pro"
# )
# messages=[SystemMessage(content="You are a helpful assistant"),
#           HumanMessage(content="Tell me about Langchain")]
# result=model.invoke(messages)
# messages.append(AIMessage(content=result.content))
# print(messages)

# we can change this using SystemMessage , HumanMessage, AIMessage

from dotenv import load_dotenv
# import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate, load_prompt

load_dotenv()
model = ChatGoogleGenerativeAI(
    model="gemini-pro-latest",  # OR: "gemini-1.5-flash", "gemini-1.5-pro"
)
chat_history=[SystemMessage(content="You are a helpful Assistant")]
while True:
    user_input = input("YOU: ")
    chat_history.append(HumanMessage(content=user_input))
    if user_input=="exit":
        break
    result=model.invoke(chat_history)
    chat_history.append(AIMessage(result.content))
    print("AI: ",result.content)
print(chat_history)