# from langchain_community.document_loaders import WebBaseLoader
# url="https://www.amazon.in/stores/Apple/page/9505ACAA-EF13-4AE6-AB5E-F14749A7822E"
# loader=WebBaseLoader(url)
# docs=loader.load()
# print(len(docs))
# print("="*100)
# print("The page content is: ",docs[0].page_content)





from langchain_community.document_loaders import PlaywrightURLLoader
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
import os

load_dotenv()
os.environ["USER_AGENT"] = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/120.0.0.0 Safari/537.36"
)

url = "https://www.amazon.in/stores/Apple/page/9505ACAA-EF13-4AE6-AB5E-F14749A7822E"
loader = PlaywrightURLLoader(urls=[url], remove_selectors=["script","style","noscript"])

docs = loader.load()
print("Docs loaded:", len(docs))
text = docs[0].page_content

model = ChatGoogleGenerativeAI(model="gemini-pro-latest")
parser = StrOutputParser()
prompt = PromptTemplate(
    template=(
        "Using only the given text, answer the question. "
        "If the answer is not explicitly in the text, reply 'Not found in the provided text'.\n\n"
        "Question: {question}\n\nText:\n{text}\n\nAnswer:"
    ),
    input_variables=["question","text"]
)
chain = prompt | model | parser
print(chain.invoke({"question":"What is the product that we are talking about?","text":text}))


print("="*120)

#For the website having heavy javascripts use playwrightURLLoader

# WebBasedLoader will not work with dynamic pages or pages with heavy javascript

from langchain_community.document_loaders import WebBaseLoader
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
import os

load_dotenv()

# IMPORTANT: Set User-Agent
os.environ["USER_AGENT"] = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/120.0.0.0 Safari/537.36"
)


url = "https://www.amazon.in/stores/Apple/page/9505ACAA-EF13-4AE6-AB5E-F14749A7822E"   # replace

# Load webpage HTML
loader = WebBaseLoader(
    web_paths=(url,),
)

docs = loader.load()

print("Total docs:", len(docs))
print("=" * 80)
print(docs[0].page_content[:1500])  # show preview

# LLM Pipeline
model = ChatGoogleGenerativeAI(model="gemini-pro-latest")
parser = StrOutputParser()

prompt = PromptTemplate(
    template=(
        "Using ONLY the given text, answer the question. "
        "If answer is missing, reply: 'Not found in the provided text.'\n\n"
        "Question: {question}\n\n"
        "Text:\n{text}\n\nAnswer:"
    ),
    input_variables=["question", "text"]
)

chain = prompt | model | parser
print("="*120)
result = chain.invoke({
    "question": "What is the page talking about?",
    "text": docs[0].page_content
})

print("\n\nANSWER:\n", result)
