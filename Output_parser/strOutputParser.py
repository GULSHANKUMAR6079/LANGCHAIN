from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate,PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
load_dotenv()
model = ChatGoogleGenerativeAI(model="gemini-pro-latest")
parser = StrOutputParser()


prompt1 = PromptTemplate(template= "Write in detailed about  the following topic. /n{text}",
                        input_variables=['text'])

prompt2 = PromptTemplate(template= "Summarize the following review in 10 lines./n{text}",
                        input_variables=['text']) 
# ONE SINGLE CHAIN
chain = prompt1 | model | parser|prompt2|model|parser

result = chain.invoke({"text":"Indian Education System"})

print(result)
