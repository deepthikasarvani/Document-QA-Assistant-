# Gen AI

Upload a PDF and ask questions about its content — the app extracts relevant context and returns an answer using a question-answering model.

## Features
- PDF upload and text extraction
- Question-answering over document content using Hugging Face Transformers QA pipeline
- Simple web interface

## Tech Stack
- Python
- Hugging Face Transformers (QA pipeline)
- (Streamlit / Flask — whichever you actually used for the interface)

## Status / Future Improvements
- Currently uses Hugging Face's QA pipeline; exploring LangChain + vector search (ChromaDB) for better context retrieval on longer documents
- Answer accuracy varies with document complexity — refinement in progress

## How to Run
1. Install dependencies: `pip install -r requirements.txt`
2. Run `python app.py` (or `streamlit run app.py`)
3. Upload a PDF and ask a question
