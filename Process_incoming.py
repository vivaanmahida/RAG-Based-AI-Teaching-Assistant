import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import joblib
import requests


# ---------------- EMBEDDING FUNCTION ----------------
def create_embedding(text_list):
    r = requests.post("http://localhost:11434/api/embed", json={
        "model": "bge-m3",
        "input": text_list
    })
    return r.json()["embeddings"]


# ---------------- LLM INFERENCE ----------------
def inference(prompt):
    r = requests.post("http://localhost:11434/api/generate", json={
        "model": "llama3.2",
        "prompt": prompt,
        "stream": False
    })
    return r.json()["response"]


# ---------------- MAIN QUERY FUNCTION ----------------
def process_query(incoming_query, top_k=5):

    df = joblib.load("embeddings.joblib")

    question_embedding = create_embedding([incoming_query])[0]

    similarities = cosine_similarity(
        np.vstack(df["embedding"]),
        [question_embedding]
    ).flatten()

    max_indx = similarities.argsort()[::-1][:top_k]
    new_df = df.loc[max_indx]

    prompt = f"""
I am teaching web development in my Sigma web development course. 
Here are video subtitle chunks containing video title, video number, 
start time in seconds, end time in seconds, the text at that time:

{new_df[["title", "number", "start", "end", "text"]].to_json(orient="records")}

---------------------------------

User Question:
"{incoming_query}"

You must:
- Answer in a human way
- Mention which video number
- Mention timestamps
- Guide the student where to go
- If unrelated, say you only answer course-related questions
"""

    response = inference(prompt)

    return response, new_df