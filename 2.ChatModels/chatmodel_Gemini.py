import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()  # .env with GOOGLE_API_KEY must be in C:\Users\gulsh\LANGCHAIN

llm = ChatGoogleGenerativeAI(
    model="gemini-pro-latest",      # one of the models your key supports
    temperature=0.7,
    max_output_tokens=256,
    # api_key optional if GOOGLE_API_KEY env var is set
    api_key=os.getenv("GOOGLE_API_KEY"),
)

resp = llm.invoke("What is the capital of India?")
print(resp.content)
