from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader
from langchain_community.document_loaders import PyPDFium2Loader

import os
from langchain_community.document_loaders import PyPDFium2Loader

# def load_books_from_folder(folder_path, password=None):
#     all_docs = []

#     # loop through all files in folder
#     for filename in os.listdir(folder_path):
#         if filename.lower().endswith(".pdf"):     # only pdfs
#             file_path = os.path.join(folder_path, filename)
#             print(f"Loading: {file_path}")

#             loader = PyPDFium2Loader(
#                 file_path=file_path,
#                 password=password
#             )
#             print("="*80)
#             docs = loader.load()
#             all_docs.extend(docs)      # append all pages from that PDF

#     return all_docs
# folder_path = "C:\\Users\\gulsh\\LANGCHAIN\\Document_Loaders\\books"

# docs = load_books_from_folder(folder_path, password="607979")
# print("="*80)
# print("Total pages loaded:", len(docs))
# print("="*80)
# print("Sample content:\n", docs[212].page_content)
# print("="*80)


# for PyPDFLoader

# loader = DirectoryLoader(
#     path='C:\\Users\\gulsh\\LANGCHAIN\\Document_Loaders\\books',
#     glob='*.pdf',
#     loader_cls=PyPDFLoader
# )
# docs=loader.load()
# print("Total pages loaded:", len(docs))
# print("="*80)

# print("First Page Content:")
# print(docs[3].page_content)

# print("\nMetadata:")
# print(docs[3].metadata)
# for document in docs:
#     print(document.metadata)



# Load VS Lazy_Load

def load_books_from_folder(folder_path, password=None):
    all_docs = []

    # loop through all files in folder
    for filename in os.listdir(folder_path):
        if filename.lower().endswith(".pdf"):     # only pdfs
            file_path = os.path.join(folder_path, filename)
            print(f"Loading: {file_path}")

            loader = PyPDFium2Loader(
                file_path=file_path,
                password=password
            )
            print("="*80)
            docs = loader.lazy_load()#lazy_load
            all_docs.extend(docs)      # append all pages from that PDF

    return all_docs
folder_path = "C:\\Users\\gulsh\\LANGCHAIN\\Document_Loaders\\books"

docs = load_books_from_folder(folder_path, password="607979")
print("="*80)
print("Total pages loaded:", len(docs))
print("="*80)
print("Sample content:\n", docs[212].page_content)
print("="*80)