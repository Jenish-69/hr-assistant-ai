from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.tools.retriever import create_retriever_tool

def create_website_retriever_tool(chunks):
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    vectorstore = FAISS.from_texts(
        texts=chunks,
        embedding=embeddings
    )

    retriever = vectorstore.as_retriever(
        search_kwargs={"k": 3}
    )

    retriever_tool = create_retriever_tool(
        retriever,
        name="website_search",
        description="Searches the scraped website content and gives relevant answers from the websites."
    )

    return retriever_tool