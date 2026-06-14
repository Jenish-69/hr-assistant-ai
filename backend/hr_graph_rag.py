import os
from typing import TypedDict, Annotated


from langgraph.graph import StateGraph, END

from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

from langchain_core.tools import tool
from langchain_groq import ChatGroq
from langgraph.checkpoint.memory import MemorySaver
memory = MemorySaver()


from typing import TypedDict, Annotated
from langgraph.graph.message import add_messages


class HRState(TypedDict):
    question: str
    context: str
    answer: str
    messages: Annotated[list, add_messages]


embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

vector_db = FAISS.load_local(
    "faiss_index",
    embeddings,
    allow_dangerous_deserialization=True
)


@tool
def search_hr_docs(question: str) -> str:
    """
    Search Zoho HR leave and attendance documentation.
    Use this tool for questions about leave, attendance,
    check-in, check-out, regularization, shifts, audit history,
    reports, approvals, and employee HR services.
    """
    results = vector_db.similarity_search(question, k=5)

    if not results:
        return "No relevant HR documentation found."

    return "\n\n".join(
        [doc.page_content for doc in results]
    )


llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0,
    api_key=os.getenv("GROQ_API_KEY")
)


def retrieve_context(state: HRState):
    question = state["question"]
    context = search_hr_docs.invoke(question)

    return {
        "context": context
    }


def generate_answer(state: HRState):
    question = state["question"]
    context = state["context"]
    messages = state["messages"]

    prompt = f"""
You are an HR Assistant.

You must answer only using the HR documentation context below.

Rules:
1. Do not invent information.
2. If the answer is not in the context, say:
   "I could not find this information in the HR documentation."
3. Keep the answer simple and clear.
4. Use step-by-step format when explaining a process.

HR Documentation Context:
{context}

Previous Conversation:
{messages}

User Question:
{question}

Answer:
"""

    response = llm.invoke(prompt)

    return {
        "answer": response.content
    }


graph = StateGraph(HRState)

graph.add_node("retrieve_context", retrieve_context)
graph.add_node("generate_answer", generate_answer)

graph.set_entry_point("retrieve_context")
graph.add_edge("retrieve_context", "generate_answer")
graph.add_edge("generate_answer", END)

app = graph.compile(
    checkpointer=memory
)