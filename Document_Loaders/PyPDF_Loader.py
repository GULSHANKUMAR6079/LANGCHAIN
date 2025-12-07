from langchain_community.document_loaders import PyPDFLoader
from langchain_core.runnables import RunnableParallel,RunnableSequence
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
load_dotenv()
model = ChatGoogleGenerativeAI(model="gemini-pro-latest")
parser = StrOutputParser()
loader=PyPDFLoader("C:\\Users\\gulsh\\LANGCHAIN\\Document_Loaders\\kelp.pdf")
docs=loader.load()
prompt=PromptTemplate(
    template="write the summary of the text in a way that summarizes whole text and also remove all the timing mentioned in the text like 0:01 or 21:04 etc ./n{text}",
    input_variables=["text"]
)
print(docs)
print("="*80)
print(len(docs))
print("="*80)
print("The page content of first page is: ",docs[0].page_content)
print("="*80)
print("The metadata of pdf is: ",docs[1].metadata)