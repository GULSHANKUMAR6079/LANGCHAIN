from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser,PydanticOutputParser
from pydantic import BaseModel,Field
from typing import Literal
from langchain_core.runnables import RunnableBranch,RunnableLambda
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-pro-latest")
parser = StrOutputParser()
class FEEDBACK(BaseModel):
    sentiment:Literal['Positive','Negative']=Field(description="Give the sentiment of the feedback")
parser2=PydanticOutputParser(pydantic_object=FEEDBACK)
    
prompt1=PromptTemplate(
    template="classify the sentiment of the following feedback into positive or negative \n {feedback} into Positive or Negative {format_instructions}",
    input_variables=["feedback"],
    partial_variables={"format_instructions":parser2.get_format_instructions()}
)
classifier_chain=prompt1|model|parser2

#to write the appropriate message for positive feedback
prompt2=PromptTemplate(template="write an appropriate message to this positive feedback.\n {feedback}and donot use * and ### this type of caracter",
                       input_variables=["feedback"]
                        )
# write the appropriate message to negative feedback
prompt3=PromptTemplate(
    template= "just write an appropriate apology message to this  negative feedback.\n {feedback} and donot use * and ### this type of caracter",
    input_variables=["feedback"]
)

#branch chain
branch_chain=RunnableBranch(
    (lambda x:x.sentiment=="Positive",prompt2|model|parser),
    (lambda x:x.sentiment=="Negative",prompt3|model|parser),
    RunnableLambda(lambda x:"could not find the sentiment")#default
)

chain=classifier_chain|branch_chain
result=chain.invoke({"feedback":"this is a great product"})
print(result)
print("="*80)
chain.get_graph().print_ascii()