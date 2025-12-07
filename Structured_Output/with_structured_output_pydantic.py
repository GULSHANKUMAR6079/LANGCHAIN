from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from typing import Annotated,Optional,Literal
from pydantic import BaseModel,Field
load_dotenv()

# Gemini Chat Model (choose gemini-1.5-pro or flash)
model = ChatGoogleGenerativeAI(
    model="gemini-pro-latest",  # OR: "gemini-1.5-flash", "gemini-1.5-pro"
)

class Review(BaseModel):
    
    
    key_themes:list[str]=Field(description="Write down all the  key themes discussed in the review in a list.")
    summary:str=Field(description="Give a brief summary of the review") 
    sentiment:Literal['pos','neg','neutral']=Field(description="Tell the mood or feeling of user or reviewer either it is positive or negative or neutral")  
    pros:Optional[list[str]]= Field(default=None,description="Write down all the pros of this review in list")
    cons:Optional[list[str]]= Field(default=None,description="Write down all the cons of this review in list")
    
structured_model=model.with_structured_output(Review) 
result = structured_model.invoke("""
                                    I recently upgraded to the Samsung Galaxy S24 Ultra, and I must say, it’s an absolute powerhouse!
                                    The Snapdragon 8 Gen 3 processor makes everything lightning fast—whether I’m gaming, multitasking, or editing photos.
                                    The 5000mAh battery easily lasts a full day even with heavy use, and the 45W fast charging is a lifesaver.
                                    The S-Pen integration is a great touch for note-taking and quick sketches, though I don't use it often.
                                    What really blew me away is the 200MP camera—the night mode is stunning, capturing crisp, vibrant images even in low light.
                                    Zooming up to 100x actually works well for distant objects, but anything beyond 30x loses quality.
                                    However, the weight and size make it a bit uncomfortable for one-handed use.
                                    Also, Samsung’s One UI still comes with bloatware—why do I need five different Samsung apps for things Google already provides?
                                    The $1,300 price tag is also a hard pill to swallow.
                                    Pros:
                                    Insanely powerful processor (great for gaming and productivity)
                                    Stunning 200MP camera with incredible zoom capabilities
                                    Long battery life with fast charging
                                    S-Pen support is unique and useful
                                    Cons:
                                    Bulky and heavy—not great for one-handed use
                                    Bloatware still exists in One UI
                                    Expensive compared to competitors."""
                                )
 
print(result)
print(type(result))
print("the summary of this is: ",result.summary)
print("The Sentiments of this sentence is: ", result.sentiment)
print("The key themes of this is: ", result.key_themes)
print("The pros of this sentence is: ", result.pros)
print("The cons of this sentence is: ", result.cons)
