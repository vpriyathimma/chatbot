import numpy as np
import pickle
import os
import json

import faiss
from sentence_transformers import SentenceTransformer
from groq import Groq


# Initialize your embedding model
model = SentenceTransformer(r'Embed_Model\Sentence_Transformer\all-MiniLM-L6-v2')

# Load the FAISS index from the saved file
index = faiss.read_index(r"question_index.faiss")

with open(r'answers.pkl', 'rb') as f:
    answers = pickle.load(f)


def get_answer(user_question):
    # Embed the user's question
    user_embedding = model.encode([user_question]).astype('float32')

    # Normalize the user's question embedding
    faiss.normalize_L2(user_embedding)

    # Search for the nearest neighbor in FAISS
    D, I = index.search(user_embedding, k=1)

    # Get the best matching question's index
    best_match_idx = I[0][0]

    # Fetch and return the corresponding answer
    return answers[best_match_idx]


def groq_llama(user_question, answer):

    prompt = {
        'role': 'user',
        'content': f''' Instruction:
                        1.If Question is not relevent under "Mobile or laptop product" then print only "This is Out of scope Question please try again with Mobile or Laptop Product" otherwise respond answer to the question
                        2.Make sure Answer is correct with Question with proper headings
                        3.Dont mention about our prompt
        Question:{user_question}
        Answer:{answer}
        #Product Recommendation
        #Conclusion
             Interactive reponse to user
        '''
    }

    # ✅ API key is read from environment variable (SAFE)
    client = Groq(api_key=os.getenv("GROQ_API_KEY"))

    chat_completion = client.chat.completions.create(
        messages=[prompt],
        model="llama-3.1-8b-instant",
    )

    result = chat_completion.choices[0].message.content
    return result


def chat_response(user_query):
    user_question = user_query
    answer = get_answer(user_question)
    chatbot_response = groq_llama(user_question, answer)
    return chatbot_response
