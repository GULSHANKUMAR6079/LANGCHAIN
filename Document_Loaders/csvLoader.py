from langchain_community.document_loaders import CSVLoader
loader=CSVLoader("C:\\Users\\gulsh\\LANGCHAIN\\Document_Loaders\\cars.csv")
docs=loader.load()
print(len(docs))
print("="*100)
print(docs[0])