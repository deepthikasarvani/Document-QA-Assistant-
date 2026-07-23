import streamlit as st
from groq import Groq
from dotenv import load_dotenv
from pathlib import Path
import os
import PyPDF2
import io

load_dotenv(Path('C:/Users/siri6/Desktop/Desktop/document-qa/.env'))
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

st.set_page_config(
    page_title="Document QA",
    page_icon="📄",
    layout="centered"
)

st.title("📄 Document QA")
st.caption("Upload any document and ask questions — AI will answer from the content.")
st.divider()

uploaded_file = st.file_uploader(
    "Upload your document",
    type=["pdf", "txt"]
)

if uploaded_file:
    # Extract text
    if uploaded_file.type == "application/pdf":
        pdf_reader = PyPDF2.PdfReader(io.BytesIO(uploaded_file.read()))
        doc_text = ""
        for page in pdf_reader.pages:
            doc_text += page.extract_text()
    else:
        doc_text = uploaded_file.read().decode("utf-8", errors="ignore")

    st.success(f"✅ Document loaded — {len(doc_text)} characters")
    st.session_state["doc_text"] = doc_text

    with st.expander("Preview document"):
        st.text(doc_text[:500] + "..." if len(doc_text) > 500 else doc_text)

if "doc_text" in st.session_state:
    st.divider()
    st.subheader("Ask a question")

    if "qa_messages" not in st.session_state:
        st.session_state.qa_messages = []

    for msg in st.session_state.qa_messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    question = st.chat_input("Ask anything about your document...")

    if question:
        st.session_state.qa_messages.append({
            "role": "user",
            "content": question
        })

        with st.chat_message("user"):
            st.markdown(question)

        with st.chat_message("assistant"):
            with st.spinner("Reading document..."):
                prompt = f"""You are a helpful document assistant.
Answer the user's question based ONLY on the document provided.
If the answer is not in the document, say "I couldn't find that in the document."

DOCUMENT:
{st.session_state['doc_text'][:4000]}

QUESTION: {question}

Give a clear, concise answer."""

                response = client.chat.completions.create(
                    model="llama-3.3-70b-versatile",
                    messages=[{"role": "user", "content": prompt}],
                    max_tokens=500
                )
                answer = response.choices[0].message.content
                st.markdown(answer)

        st.session_state.qa_messages.append({
            "role": "assistant",
            "content": answer
        })

else:
    st.info("👆 Upload a document to get started")
