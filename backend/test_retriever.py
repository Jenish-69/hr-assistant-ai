from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

vector_db = FAISS.load_local(
    "faiss_index",
    embeddings,
    allow_dangerous_deserialization=True
)

query = "How do I regularize attendance?"

results = vector_db.similarity_search(query, k=3)

print("Search results:")
print("--------------------------------")

for i, doc in enumerate(results):
    print("Result", i + 1)
    print(doc.page_content[:700])
    print("--------------------------------")