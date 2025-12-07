from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel
from dotenv import load_dotenv
load_dotenv()
model = ChatGoogleGenerativeAI(model="gemini-pro-latest")
prompt1=PromptTemplate(
    template="Write asimple , clean, useful and undetstandable notes in detailexplaining about the {topic} and use examples along with the explanantion and  Do not use # and * while returning the output donot give it in markdown format",
    input_variables=["topic"]
)
parser = StrOutputParser()



prompt2=PromptTemplate(
    template="Generate 5 question and answer regarding that  {topic} which can let student understand that topic easily. and Do not use # and * while returning the output donot give it in markdown format",
    input_variables=["topic"]
)

prompt3=PromptTemplate(
    template="Generate notes and quiz regarding topic which can let student understand that topic easily in single documents notes->{chain_notes} and quiz->{chain_quiz}. and Do not use # and * while returning the output donot give it in markdown format",
    input_variables=["chain_notes","chain_quiz"]
)
parallel_chain=RunnableParallel({
    'chain_notes':prompt1|model|parser,
    'chain_quiz':prompt2|model|parser
})
merge_chain=prompt3|model|parser

final_chain=parallel_chain|merge_chain

result=final_chain.invoke({"topic":"Linear Regression"})
print(result)
print("="*80)

final_chain.get_graph().print_ascii()
