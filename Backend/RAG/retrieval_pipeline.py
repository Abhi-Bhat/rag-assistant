import langchain_ollama
from langchain_community.document_loaders import PyPDFLoader,DirectoryLoader
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_chroma import Chroma
# from transformers import pipeline
from langchain_ollama import OllamaLLM
embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
from os import path

BASE_DIR = path.dirname(path.dirname(path.dirname(path.abspath(__file__))))
persist_directory = path.join(BASE_DIR, "db", "chroma_db")

db = Chroma(
    persist_directory = persist_directory,
    embedding_function=embedding_model,
    collection_metadata={"hnsw:space":"cosine"}
)

model = OllamaLLM(model="phi3")

def get_answer(query: str):
    query = query
    results = db.similarity_search(query,k=2)
    context = "\n\n".join([doc.page_content for doc in results])

    sources = set()

    for doc in results:
        page = doc.metadata.get("page", None)
        if page is not None:
            sources.add(page)

    prompt = f"""
    You are an AI assistant.
    
    Answer in a short and clear way using the context given
    If answer is not explicitly in context → say I don’t know
    
    Context:
    {context}
    
    Question:
    {query}
    
    Answer:
    """

    answer = model.invoke(prompt)
    return answer,list(sources)

if __name__ == "__main__":
    print(get_answer("What is operating system?"))