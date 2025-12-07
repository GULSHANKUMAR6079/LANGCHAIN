from langchain_huggingface import HuggingFaceEmbeddings
embedding=HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')


text="what is the property of alkanes ?" 
vector1=embedding.embed_query(text)
print(str(vector1))


docs=["what is the property of alkanes ?"]
vector2=embedding.embed_documents(docs)
print(str(vector2))