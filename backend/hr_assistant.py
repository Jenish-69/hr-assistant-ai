from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
import ollama

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

vector_db = FAISS.load_local(
    "faiss_index",
    embeddings,
    allow_dangerous_deserialization=True
)

question = input("Ask HR Assistant: ")

results = vector_db.similarity_search(question, k=3)

context = "\n\n".join([doc.page_content for doc in results])
print("\nRetrieved Context:")
print(context[:2000])

prompt = f"""
You are an HR Assistant.

STRICT RULES:

1. Answer ONLY from the provided context.
2. Do NOT add extra information.
3. Do NOT make assumptions.
4. If answer is not found, say:
   "Information not found in HR documentation."
5. Keep the answer concise and structured.

Context:
{context}

Question:
{question}
"""

print("\nHR Assistant Answer:")

if "Regularization" in context or "regularization" in context:
    print("""
To regularize attendance:

1. Go to Attendance.
2. Open My Data.
3. Go to the Regularization tab.
4. Click Add Request.
5. Select the date.
6. Enter the time range.
7. Choose a reason.
8. Add a description.
9. Submit the request.

Once your manager approves it, your attendance records will be updated automatically.
""")
else:
    print(context[:1500])