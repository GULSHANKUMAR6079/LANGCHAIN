import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

# Load .env file
load_dotenv()

# Use environment variable
llm = ChatGoogleGenerativeAI(model='gemini-pro-latest')

response = llm.invoke("What is the capital of India")
print(response.content)

