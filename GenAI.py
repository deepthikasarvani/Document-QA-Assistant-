!pip install langchain transformers torch
!pip install langchain langchain-community langchain-openai openai transforms torch
!pip install cromadb
!pip install sentence-transformers
import chromadb
from chromadb.config import settings
from sentence_transformers import SentenceTransformer
chroma_client = chromadb.Client(Settings(anonymized_telemetry=False))
collection = chroma_client.get_or_create_collection(name="docs")
embedding_model = SentenceTransformer('all-MiniLM-L6-v2')
document_text = """ 
Generative AI referes to artificial intelligence models that can generate new content,
like text, images, or music, based on patterns learned from input data.
It is commonly used in creating realistic text, images, and other content with minimal input.
Generative AI models include GPT-4 and DALL-E, which are used for writing articles, creating images, and even programming.
"""
document_embedding = embedding_model.encode(document_text)
collection.add(
   documents=[document_text],
   embeddings=[document_embedding.tolist()]
   ids=["genai_doc_1"]
)

question = "What is Generative AI?"
question_embedding = embedding_model.encode(question)

results = collection.query(
   query_embeddings=[question_embedding.tolist()]
   n_results=1
)
relevant_doc = results["documents"][0][0]

from langchain.chat_models import ChatOpenAI
from langchain.chains import ConversationChain
from transformers import pipeline

qa_pipeline = pipeline("question-answering")
document_text="""
Generative AI referes to artificial intelligence models that can generate new content,
like text, images, or music, based on patterns learned from input data.
It is commonly used in creating realistic text, images, and other content with minimal input.
Generative AI models include GPT-4 and DALL-E, which are used for writing articles, creating images, and even programming.
"""

question = "What is Generative AI?"

result = qa_pipeline(question=question, context=document_text)
print("Answer:", result['answer'])

model = ChatOpenAI(model="gpt-4", temperature=0.7)
conversation_answer = ConversationChain(llm=model)

conversation_answer = conversation_chain.predict(input=f"Document:\n{document_text}\n\nQuestion: {question}")
print("LangChain Answer:", conversation_answer)

