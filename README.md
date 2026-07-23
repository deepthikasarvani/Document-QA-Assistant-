# 📄 Document QA — AI Document Assistant

Upload any PDF or text file and ask questions — AI answers directly from your document.

## What it does
- Upload a PDF or TXT file
- Ask any question about the document
- AI reads the document and answers accurately
- Multi-turn conversation — ask multiple questions in one session

## Tech Stack
- Python
- Streamlit
- Groq API (LLaMA 3.3)
- PyPDF2 (PDF text extraction)

## How to run
1. Clone the repo
2. Install dependencies:
   `pip install streamlit groq python-dotenv PyPDF2`
3. Create `.env` file:
   `GROQ_API_KEY=your_groq_key_here`
4. Run:
   `python -m streamlit run app.py`

## How it works
This project uses RAG (Retrieval Augmented Generation) — the document text is extracted and passed as context to the LLM, allowing it to answer questions specifically from your content rather than general knowledge.

## Use cases
- Study notes summarization
- Contract/legal document analysis
- Research paper Q&A
- Any document you need to understand fast
