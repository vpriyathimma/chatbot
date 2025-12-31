# Product Recommendation Chatbot

**Author:** Vishnupriya T  
**GitHub:** https://github.com/vpriyathimma  
**Email:** vpriyathimma@gmail.com  

---

##  Project Overview

This project is an intelligent **product recommendation chatbot** designed to assist users with **mobile and laptop-related queries**.  
It combines **semantic search** using sentence embeddings with **LLM-based response generation** to deliver accurate, context-aware recommendations.

The system retrieves the most relevant product information using vector similarity search and refines responses using a large language model for better readability and structure.

---

##  System Architecture

1. **Sentence Embeddings**
   - User queries are converted into dense embeddings using a Sentence Transformer model.
2. **Vector Search (FAISS)**
   - A FAISS index is used to retrieve the most semantically similar product-related information.
3. **LLM Response Generation**
   - Retrieved content is enhanced and structured using a Groq-hosted LLaMA model.
4. **Web Interface**
   - A Flask-based web application enables user interaction through a browser.

---

##  Tech Stack

- **Programming Language:** Python  
- **NLP & Embeddings:** SentenceTransformers (MiniLM)  
- **Vector Database:** FAISS  
- **LLM API:** Groq (LLaMA 3.1)  
- **Web Framework:** Flask  
- **Frontend:** HTML, CSS  

---

##  Security & Best Practices

- API keys are **not hardcoded** in the source code.
- Secrets are managed using **environment variables**.
- Large models, datasets, and sensitive artifacts are excluded from version control using `.gitignore`.

This follows **industry-standard secure development practices**.

---

##  How to Run the Project

### 1️ Install dependencies
```bash
pip install -r requirement.txt
