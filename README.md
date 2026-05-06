1.	Objective:
Allow users to upload documents (PDFs, Word files) and ask questions based on the content.

2.	Tech Stack:
LangChain, OpenAI API (GPT-4), ChromaDB or FAISS, Streamlit.

3.	Tools Used:
•	Python: Used for developing the entire project, managing logic, and integrating different libraries.
•	LangChain: Used to orchestrate conversational AI flows by integrating with OpenAI’s GPT-4 model.
•	OpenAI GPT-4 API: Provides the powerful large language model behind the conversational responses.
•	Hugging Face Transformers: Utilized the question-answering pipeline for extracting answers from documents.
•	Streamlit: Used to build the interactive web app interface for user input and displaying answers.
•	•  ChromaDB: Serves as a lightweight vector database to store and retrieve document embeddings for contextual Q&A.
•	•  Sentence Transformers: Converts documents and queries into embeddings for semantic similarity with ChromaDB.

