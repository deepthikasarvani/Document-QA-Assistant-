import streamlit as st
from transformers import pipeline
from langchain.chat_models import ChatOpenAI
from langchain.chains import ConversationChain
import chromadb
from chromadb.config import Settings
from sentence_transformers import SentenceTransformer

# ChromaDB setup
chroma_client = chromadb.Client(Settings(anonymized_telemetry=False))
collection = chroma_client.get_or_create_collection(name="docs")
embedding_model = SentenceTransformer('all-MiniLM-L6-v2')

# Initialize Hugging Face QA pipeline
qa_pipeline = pipeline("question-answering")

# Set Streamlit page config
st.set_page_config(page_title="GenAI Q&A App", page_icon="🧠")

# Pastel CSS styling for the Streamlit app
st.markdown("""
    <style>
    .stApp {
        background-color: #fdf6f9;
        color: #222;
        font-family: 'Segoe UI', sans-serif;
    }
    .stTextArea, .stTextInput {
        background-color: #fff0f6 !important;
        border-radius: 10px !important;
    }
    .stButton>button {
        background-color: #d1c4e9;
        color: black;
        border-radius: 10px;
    }
    .stButton>button:hover {
        background-color: #b39ddb;
        color: white;
    }
    </style>
""", unsafe_allow_html=True)

# Streamlit Interface
st.title("🧠 Generative AI - Document Question Answering")

# Document input area
document = st.text_area("📄 Paste your document below:", height=200)

# Question input
question = st.text_input("❓ Enter your question:")

# ChromaDB Document Embedding & Query
if document and question:
    # Document embedding for ChromaDB
    document_embedding = embedding_model.encode(document)
    
    # Add document to ChromaDB if new
    collection.add(
        documents=[document],
        embeddings=[document_embedding.tolist()],
        ids=["user_document"]
    )
    
    # Question embedding for semantic search
    question_embedding = embedding_model.encode(question)
    
    # Query ChromaDB for most relevant document
    results = collection.query(
        query_embeddings=[question_embedding.tolist()],
        n_results=1
    )
    
    # Get the most relevant document
    relevant_doc = results["documents"][0][0]
    
    # Hugging Face QA
    result = qa_pipeline(question=question, context=relevant_doc)
    
    # LangChain for conversation-based Q&A
    model = ChatOpenAI(model="gpt-4", temperature=0.7)
    conversation_chain = ConversationChain(llm=model)
    conversation_answer = conversation_chain.predict(input=f"Document:\n{relevant_doc}\n\nQuestion: {question}")
    
    # Show answers in Streamlit
    st.subheader("📝 Hugging Face QA Answer:")
    st.write(result['answer'])
    
    st.subheader("💬 LangChain GPT-4 Answer:")
    st.write(conversation_answer)
    
# Button to trigger
if st.button("Get Answer"):
    if not document.strip() or not question.strip():
        st.warning("Please provide both a document and a question.")
