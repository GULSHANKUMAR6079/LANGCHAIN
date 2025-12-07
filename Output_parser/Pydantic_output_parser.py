from langchain_huggingface import HuggingFaceEndpoint,ChatHuggingFace
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
load_dotenv()
llm1=HuggingFaceEndpoint(repo_id="google/gemma-2-2b-it",task="text_generation")
model=ChatHuggingFace(llm=llm1)

class Person(BaseModel):
    name:str=Field(description="Name of the Person")
    age:int = Field(gt=18,description="Age of the person")
    city:str = Field(description="The city which person Belongs to")
parser=PydanticOutputParser(pydantic_object=Person) 
template1=PromptTemplate(
    template="generate the  name ,age ,and city of a fictional {place} person \n {format_instruction}",
    input_variables=["place"],
    partial_variables= {"format_instruction":parser.get_format_instructions()}
)

prompt=template1.invoke({"place":"Indian"})
result=model.invoke(prompt)
print("="*70)
print("The prompt passsed to llm is :",prompt)
print("="*70)
f_result=parser.parse(result.content)
print(f_result)
print(type(f_result))
print("The name of fictional character is : ",f_result.name)
print("="*80)
# but why to write that much of code we can just chain them 
chain=template1|model|parser
result=chain.invoke({"place":"Indian"})#require one argument atleast if not send {}
print(result)
print(result.name)



# template2=PromptTemplate(
#     template="give me 10 facts about {topic} \n {format_instruction}",
#     input_variables=["topic"],
#     partial_variables= {"format_instruction":parser.get_format_instructions()}
# )

# chain=template2|model|parser
# result1=chain.invoke({"topic":"Indian Education"})#require one argument atleast if not send {}
# print("="*80)
# print(result1)
