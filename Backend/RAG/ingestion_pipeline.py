from langchain_community.document_loaders import PyPDFLoader,DirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from os import path

BASE_DIR = path.dirname(path.dirname(path.dirname(path.abspath(__file__))))
docs_path = path.join(BASE_DIR, "docs")


'''
LOAD OS Manual
Load ppt

Chunking

Embedding
'''
def doc_ingestion(docs_path):
    loader = DirectoryLoader(path = docs_path, loader_cls=PyPDFLoader)
    docs = loader.load()
    return docs

def chunking(docs,chunk_size,chunk_overlap ):
    chunker = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
    chunks = chunker.split_documents(docs)
    return chunks

def vector_db(chunks,persist_directory="db/chroma_db"):
    embedding_model = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    vector_store = Chroma.from_documents(
        documents=chunks,
        embedding=embedding_model,
        persist_directory=persist_directory,
        collection_metadata={"hnsw:space":"cosine"}
    )

    return vector_store


if __name__ == '__main__':
    docs = doc_ingestion(docs_path)
    chunks = chunking(docs,500,50)
    vector_store = vector_db(chunks)