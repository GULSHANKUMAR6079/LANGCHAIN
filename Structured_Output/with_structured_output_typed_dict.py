from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from typing import TypedDict
load_dotenv()

# Gemini Chat Model (choose gemini-1.5-pro or flash)
model = ChatGoogleGenerativeAI(
    model="gemini-pro-latest",  # OR: "gemini-1.5-flash", "gemini-1.5-pro"
)

class Review(TypedDict):
    summary:str
    sentiment:str  
structured_model=model.with_structured_output(Review) 
result = structured_model.invoke("""The hardware is great, but the software feels bloated. 
                            There are too many pre-installed apps that I can't remove. 
                            Also, the UI looks outdated compared to other brands. 
                            Hoping for a software update to fix this.""")
 
print(result)
print(type(result))
print("the summary of this is: ",result['summary'])
print("The Sentiments of this sentence is: ", result["sentiment"])