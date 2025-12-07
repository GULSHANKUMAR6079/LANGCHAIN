from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
load_dotenv()
model = ChatGoogleGenerativeAI(model="gemini-pro-latest")
prompt=PromptTemplate(
    template="Give me 5 interesting topic about {topic} Do not use # and * while returning the output donot give it in markdown format",
    input_variables=["topic"]
)
parser = StrOutputParser()
chain=prompt|model|parser
result=chain.invoke({"topic":"Cricket"})
chain.get_graph().print_ascii()
print(result)
print("="*80)
