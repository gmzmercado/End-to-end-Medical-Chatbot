# You only have to execute this .py only one time.
# Should you have more files to add to `Data` folder,
# that's the time you execute this file again.

from src.helper import load_pdf_file, text_split, download_hugging_face_embeddings
from pinecone.grpc import PineconeGRPC as Pinecone
from pinecone import ServerlessSpec
from langchain_pinecone import PineconeVectorStore
from dotenv import load_dotenv
import os

# Attain API Keys from .env
load_dotenv()
PINECONE_API_KEY = os.environ.get('PINECONE_API_KEY')
os.environ["PINECONE_API_KEY"] = PINECONE_API_KEY

# Extract Data
extracted_data = load_pdf_file(data='Data/')

# Split Data into Text Chunks
text_chunks = text_split(extracted_data)

# Download Embeddings from HuggingFace
embeddings = download_hugging_face_embeddings()

# Initialize Pinecone and Create Index (This is your Knowledge Base)
index_name = "medicalbot"
pc = Pinecone(api_key=PINECONE_API_KEY)
pc.create_index(
    name=index_name,
    dimension=384,
    metric="cosine",
    spec=ServerlessSpec(
        cloud="aws",
        region="us-east-1"
    ),
)

# Embed each chunk and upsert the embeddings into your Pinecone index
docsearch = PineconeVectorStore.from_documents(
    documents=text_chunks,
    index_name=index_name,
    embedding=embeddings,
)