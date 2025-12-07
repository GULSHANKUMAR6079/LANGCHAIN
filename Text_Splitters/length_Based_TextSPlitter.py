from langchain_text_splitters import CharacterTextSplitter
text="""Text splitters are tools used to break large documents into smaller and more manageable pieces so that they can be processed efficiently by language models. Since LLMs have a limited context window and cannot handle very long documents at once, text splitting becomes an essential step in any retrieval or summarization pipeline. A text splitter divides the document based on certain rules such as character length, token count, sentences, or paragraphs. The goal is to create chunks that are small enough for the model to handle, yet meaningful enough to preserve context. Well-structured chunks help improve the accuracy of embeddings, retrieval, and final responses from the model. Without splitting, important parts of the document might be ignored due to context limits, leading to incomplete or incorrect answers.

One common method is length-based text splitting, where the document is divided purely by size, such as by characters or tokens. Although simple and fast, this approach has significant disadvantages. Length-based splitting often breaks sentences or paragraphs in unnatural places, which can disrupt the meaning of the content. As a result, the model receives incomplete ideas, lowering the quality of embeddings and making retrieval less accurate. This can also lead to hallucinations or irrelevant responses in RAG systems. Additionally, to preserve context, developers usually add overlaps between chunks, which increases the number of chunks and raises computational and embedding costs. Because length-based splitting does not understand the structure or meaning of the document, it is less suitable for complex or structured text such as legal documents, research papers, code, or technical content.

More advanced text splitters try to preserve semantic boundaries by splitting along paragraphs, sentences, or headings. These produce chunks that represent complete ideas and lead to better performance in LLM pipelines. However, they may require more computation. Overall, text splitting is a crucial step in preparing long documents for language models, and choosing the right type of splitter directly affects the accuracy and efficiency of downstream tasks."""

splitter=CharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=0,
    separator=","
)
result=splitter.split_text(text)
print("="*100)
print(result)

str="Text splitters are tools used to break large documents into smaller and more manageable pieces so that they can be processed efficiently by language models. Since LLMs have a limited context window and cannot handle very long documents at once"
print("="*100)
print(len(str))

# how to do for pdf 
from langchain_community.document_loaders import PyPDFLoader
loader=PyPDFLoader(file_path="C:\\Users\\gulsh\\LANGCHAIN\\Document_Loaders\\kelp.pdf")
docs=loader.load()
print("="*100)
result=splitter.split_documents(docs)
print(result[12].page_content)

