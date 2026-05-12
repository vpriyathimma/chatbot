# Product Recommendation Chatbot

Product Recommendation Chatbot is an intelligent RAG-based application designed to simplify product research by delivering context-aware mobile and laptop recommendations without endless tab switching.

Built to solve the frustration of comparing products across multiple tabs, this chatbot leverages Retrieval-Augmented Generation (RAG), semantic vector search, and LLM-powered reasoning to understand user preferences beyond keyword matching.

By combining FAISS vector search, SentenceTransformers embeddings, and Llama 3.1 via Groq, the system provides fast, relevant, and personalized product recommendations for smarter purchasing decisions.

---

## Features

- Context-aware product recommendations for mobiles and laptops  
- Semantic product search using vector embeddings  
- Retrieval-Augmented Generation (RAG) for accurate personalized responses  
- Fast vector similarity search with FAISS  
- Real-time LLM recommendations powered by Llama 3.1 via Groq  
- Secure API key management using `.env`  
- Lightweight Flask backend for easy deployment  
- Scalable architecture for future product category expansion  

---

## Tech Stack

### Backend
- Flask  

### Vector Search
- FAISS (Facebook AI Similarity Search)  

### Large Language Model
- Llama 3.1 via Groq API  

### Embeddings
- SentenceTransformers (MiniLM)  

### Development Environment
- Python  
- Virtual Environment / Local Deployment  

---

## How It Works

1. Users enter a product-related query (e.g., “Best gaming laptop under 80K”)  
2. Query is transformed into semantic vector embeddings  
3. FAISS retrieves the most relevant product data  
4. Llama 3.1 processes retrieved context for reasoning  
5. Chatbot generates personalized product recommendations instantly  

---

## Installation & Setup

### Clone the Repository
```bash
git clone https://github.com/vpriyathimma/chatbot.git
cd chatbot
```

### Development Requirements
- Python 3.9+  
- pip  
- Groq API Key  
- Virtual environment (recommended)  

### Install Dependencies
```bash
pip install -r requirements.txt
```

### Configure Environment Variables
Create a `.env` file in the root directory:

```env
GROQ_API_KEY=your_api_key_here
```

### Run the Application
```bash
python app.py
```

### Access the App
```bash
http://localhost:5000
```

---

## Project Structure

```bash
chatbot/
│── app.py
│── requirements.txt
│── .env
│── data/
│── embeddings/
│── templates/
└── README.md
```

---

## Current Scope

### Core Focus:
- Mobile phone recommendations  
- Laptop recommendations  
- Semantic product understanding  
- Fast personalized search  
- Real-time conversational product assistance  

### Planned Enhancements:
- Tablet recommendations  
- Smartwatch comparisons  
- Multi-category product support  
- UI/UX enhancements  
- E-commerce integration  

---

## Security & Privacy

- Secure API key management through `.env`  
- No hardcoded credentials  
- Privacy-conscious local deployment  
- Controlled external API integration  
- Expandable for enterprise-grade deployment security  

---

## Future Improvements

- Front-end dashboard for richer user interaction  
- User preference memory system  
- Price tracking integrations  
- Advanced recommendation filters (budget, specs, brands)  
- Voice-enabled assistant  
- Deployment on cloud platforms  

---

## Why This Project Matters

This project demonstrates practical implementation of advanced AI engineering concepts including Retrieval-Augmented Generation, vector databases, semantic search, and LLM deployment for real-world consumer applications.

It highlights expertise in:
- RAG Architecture  
- Flask Development  
- FAISS Vector Search  
- NLP Embeddings  
- Groq API Integration  
- AI Product Recommendation Systems  

---

## Why Groq?

Groq’s Llama 3.1 implementation was selected for its exceptional speed and responsiveness, making it ideal for real-time product recommendation workflows where latency directly impacts user experience.

---

## Author

**Vishnupriya T**

- GitHub: https://github.com/vpriyathimma  
- Email: vpriyathimma@gmail.com  
- LinkedIn: https://www.linkedin.com/in/vishnupriya-t-7a0b8925b/  

---

## License

This project is intended for educational, portfolio, and AI-powered product research purposes. You may modify and expand it for personal or professional development.

