import requests

def create_embedding(text_list):
    embeddings = []
    for text in text_list:
        r = requests.post("http://localhost:11434/api/embeddings", json={
            "model": "bge-m3",
            "prompt": text  # Use 'prompt' instead of 'input'
        })
        response = r.json()
        embeddings.append(response.get("embedding", []))
    return embeddings