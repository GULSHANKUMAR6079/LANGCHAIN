from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
load_dotenv()
model = ChatGoogleGenerativeAI(model="gemini-pro-latest")
prompt1=PromptTemplate(
    template="Write in detail about the  {topic} Do not use # and * while returning the output donot give it in markdown format",
    input_variables=["topic"]
)
parser = StrOutputParser()


prompt2=PromptTemplate(
    template="Generate 10 point summary in brief containing all the depth  about the {topic} Do not use # and * while returning the output donot give it in markdown format",
    input_variables=["topic"]
)
chain=prompt1|model|parser|prompt2|model|parser

result=chain.invoke({"topic":"Elon_musk"})
print(result)
print("="*80)

chain.get_graph().print_ascii()

