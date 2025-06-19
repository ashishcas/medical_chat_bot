from src.helper import load_pdf, text_split, download_hugging_face_embeddings
from langchain.vectorstores import Pinecone
from pinecone import Pinecone
from langchain_pinecone import PineconeVectorStore

from dotenv import load_dotenv
import os

load_dotenv()

PINECONE_API_KEY = os.environ.get('PINECONE_API_KEY')

extracted_data = load_pdf("data/")
text_chunks = text_split(extracted_data)
embeddings = download_hugging_face_embeddings()


pc = Pinecone(api_key="pcsk_5QgM8_L9Mbyn9J9EejcYvyaYfnVzbMG43gnZHMcdyzQgLM8nAf2KUmja1AXdBtxRMA1ka")
index = pc.Index("medical-bot-project")

texts = [t.page_content for t in text_chunks]  # from LangChain text splitter
 
vectorstore_from_texts = PineconeVectorStore.from_texts(
        texts,
        index_name="medical-bot-project",
        embedding=embeddings
    )
print(vectorstore_from_texts)