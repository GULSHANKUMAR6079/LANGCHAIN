from langchain_huggingface import HuggingFaceEndpoint,ChatHuggingFace
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
load_dotenv()
llm1=HuggingFaceEndpoint(repo_id="google/gemma-2-2b-it",task="text_generation")
model=ChatHuggingFace(llm=llm1)
parser=JsonOutputParser()
template1=PromptTemplate(
    template="give me name ,age ,and city of a fictional person \n {format_instruction}",
    input_variables=[],
    partial_variables= {"format_instruction":parser.get_format_instructions()}
)

prompt=template1.format()
result=model.invoke(prompt)
f_result=parser.parse(result.content)
print(f_result)
print(type(f_result))
print("The name of fictional character is : ",f_result["name"])
print("="*80)
# but why to write that much of code we can just chain them 
chain=template1|model|parser
result=chain.invoke({})#require one argument atleast if not send {}
print(result)
print(result["name"])



template2=PromptTemplate(
    template="give me 10 facts about {topic} \n {format_instruction}",
    input_variables=["topic"],
    partial_variables= {"format_instruction":parser.get_format_instructions()}
)

chain=template2|model|parser
result1=chain.invoke({"topic":"Indian Education"})#require one argument atleast if not send {}
print("="*80)
print(result1)
