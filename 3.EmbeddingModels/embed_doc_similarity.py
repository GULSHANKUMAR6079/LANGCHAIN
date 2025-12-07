from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

# Load free Hugging Face model
embedding_model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

# Your documents
documents = [
    "Virat Kohli is an Indian cricketer known for his aggressive batting and leadership.",
    "MS Dhoni is a former Indian captain famous for his calm demeanor and finishing skills.",
    "Sachin Tendulkar, also known as the 'God of Cricket', holds many batting records.",
    "Rohit Sharma is known for his elegant batting and record-breaking double centuries.",
    "Jasprit Bumrah is an Indian fast bowler known for his unorthodox action and yorkers."
]

# Query
query = "tell me about sachin"

# Get embeddings
doc_embeddings = embedding_model.encode(documents, convert_to_numpy=True)
query_embedding = embedding_model.encode([query], convert_to_numpy=True)

# Compute similarity
scores = cosine_similarity(query_embedding, doc_embeddings)[0]

# Find best match
index, score = sorted(list(enumerate(scores)), key=lambda x: x[1])[-1]

# Output
print("Query:", query)
print("Best match:", documents[index])
print("Similarity score:", score)
