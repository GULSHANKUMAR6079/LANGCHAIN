<<<<<<< HEAD
# import langchain

# print(langchain.__version__)
import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

models = genai.list_models()

for m in models:
    if hasattr(m, "supported_generation_methods") and "generateContent" in m.supported_generation_methods:
        print(m.name)
=======
# import langchain

# print(langchain.__version__)
import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

models = genai.list_models()

for m in models:
    if hasattr(m, "supported_generation_methods") and "generateContent" in m.supported_generation_methods:
        print(m.name)
>>>>>>> 6c3e6436 (first commit)
