from langchain_experimental.text_splitter import SemanticChunker
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embed_model = GoogleGenerativeAIEmbeddings(
    model="models/text-embedding-004"  # correct embedding model
)

text_splitter = SemanticChunker(
    embed_model,
    breakpoint_threshold_type="standard_deviation",
    breakpoint_threshold_amount=1   # more reasonable threshold
)

sample = """
Farmers were working hard in the fields, preparing the soil and planting seeds for the next season
The sun was bright, and the air smelled of earth and fresh grass. 
The Indian Premier League (IPL) is the biggest cricket league in the world. 
People all over the world watch the matches and cheer for their favourite teams.

Terrorism is a big danger to peace and safety. 
It causes harm to people and creates fear in cities and villages. 
When such attacks happen, they leave behind pain and sadness. 
To fight terrorism, we need strong laws, alert security forces, and support from people who care about peace and safety.
"""

docs = text_splitter.create_documents([sample])
print(len(docs))
for d in docs:
    print("\n=== Chunk ===\n", d.page_content)
