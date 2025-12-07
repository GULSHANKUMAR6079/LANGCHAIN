from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv
import os

load_dotenv()

# Gemini embedding model (current best)
# Equivalent to OpenAIEmbeddings(model="...", dimensions=...)
embed = GoogleGenerativeAIEmbeddings(
    model="text-embedding-004",   # Google's latest embedding model
    api_key=os.getenv("GOOGLE_API_KEY"),
)
docs=["delhi is the capital of India","patna is the capital of Bihar","Ram eats a mango"]
result = embed.embed_documents(docs)

# print("Embedding length:", len(result))
print("Embedding vector:", result[:2], "...")   # show only first 10 numbers
