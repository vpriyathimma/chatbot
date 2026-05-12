# Product Recommendation Chatbot 

I put this together because I was tired of opening 50 tabs every time I wanted to compare phone specs. It's a simple chatbot that uses RAG (Retrieval-Augmented Generation) to actually understand what you're looking for in a mobile or laptop and give you a straight answer.

Instead of just searching keywords, it uses vector embeddings to "understand" the context of your question.

### The Stack
*   **Backend:** Flask
*   **Search:** FAISS (for the fast vector lookups)
*   **Brain:** Llama 3.1 via Groq (the speed is honestly impressive)
*   **Embeddings:** SentenceTransformers (MiniLM)

---

### How to run it
1.  Grab the code: `git clone https://github.com/vpriyathimma/chatbot.git`
2.  Install the stuff: `pip install -r requirements.txt`
3.  Add your Groq API key to a `.env` file (`GROQ_API_KEY=your_key_here`)
4.  Run `python app.py` and hit `localhost:5000`

---

### A few notes
*   **Why Groq?** I tried a few different ways to run the LLM, but Groq’s Llama 3.1 implementation was the fastest for getting real-time recommendations.
*   **Data:** Right now it’s focused on mobiles and laptops. I’m thinking of expanding the dataset later.
*   **Privacy:** I've used `.env` for keys, so no secrets are leaked in the code.

### To-do list
- [ ] Add more product categories (maybe cameras?)
- [ ] Make the UI a bit more "chat-like"
- [ ] Add a "compare" feature for two specific models

---
**Vishnupriya T**  
[vpriyathimma@gmail.com](mailto:vpriyathimma@gmail.com) | [@vpriyathimma](https://github.com/vpriyathimma)
