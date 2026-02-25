# import requests # type: ignore
# import os
# import json
# import pandas as pd

# def create_embedding(text_list):
#     # https://github.com/ollama/ollama/blob/main/docs/api.md#generate-embeddings
#     r = requests.post("http://localhost:11434/api/embed", json={
#         "model": "bge-m3",
#         "input": text_list
#     })

#     embedding = r.json()["embeddings"] 
#     return embedding


# jsons = os.listdir("jsons")  # List all the jsons 
# my_dicts = []
# chunk_id = 0

# for json_file in jsons:
#     with open(f"jsons/{json_file}") as f:
#         content = json.load(f)
#     print(f"Creating Embeddings for {json_file}")
#     embeddings = create_embedding([c['text'] for c in content['chunks']])
       
#     for i, chunk in enumerate(content['chunks']):
#         chunk['chunk_id'] = chunk_id
#         chunk['embedding'] = embeddings[i]
#         chunk_id += 1
#         my_dicts.append(chunk) 
# # print(my_dicts)

# df = pd.DataFrame.from_records(my_dicts)
# print(df)
# a = create_embedding(["Cat sat on the mat", "Harry dances on a mat"])
# print(a)

#==========================================================================================HARRY CODE UP===============================================================================================#


# import requests # type: ignore
# import os
# import json
# import pandas as pd

# def create_embedding(text_list):
#     # Filter out empty or invalid texts
#     valid_texts = []
#     valid_indices = []
    
#     for i, text in enumerate(text_list):
#         if text and isinstance(text, str) and len(text.strip()) > 0:
#             # Limit text length (Ollama typically has a token limit)
#             valid_texts.append(text.strip()[:5000])  # Limit to 5000 chars
#             valid_indices.append(i)
    
#     if not valid_texts:
#         return [[] for _ in text_list]  # Return empty embeddings
    
#     try:
#         r = requests.post("http://localhost:11434/api/embed", json={
#             "model": "bge-m3",
#             "input": valid_texts
#         })
        
#         response = r.json()
        
#         if "error" in response:
#             print(f"API Error: {response['error']}")
#             return [[] for _ in text_list]
        
#         embeddings_result = response.get("embeddings", [])
        
#         # Map embeddings back to original indices
#         full_embeddings = [[] for _ in text_list]
#         for idx, emb_idx in enumerate(valid_indices):
#             full_embeddings[emb_idx] = embeddings_result[idx]
        
#         return full_embeddings
        
#     except Exception as e:
#         print(f"Error creating embeddings: {e}")
#         return [[] for _ in text_list]

# jsons = os.listdir("jsons")
# my_dicts = []
# chunk_id = 0

# for json_file in jsons:
#     with open(f"jsons/{json_file}") as f:
#         content = json.load(f)
#         print(f"Creating Embedding for {json_file}")
        
#         # Debug: Check the chunks
#         chunks = content.get('chunks', [])
#         print(f"Number of chunks: {len(chunks)}")
        
#         # Get embeddings for all chunks at once
#         texts = [c.get('text', '') for c in chunks]
#         embeddings = create_embedding(texts)
        
#         for i, chunk in enumerate(chunks):
#             if embeddings[i]:  # Only add if embedding was created
#                 chunk['chunk_id'] = chunk_id
#                 chunk['embedding'] = embeddings[i]
#                 chunk_id += 1
#                 my_dicts.append(chunk)
#             else:
#                 print(f"Warning: Skipping chunk {i} - no embedding created")

# df = pd.DataFrame.from_records(my_dicts)
# print(df)
# print(f"\nTotal chunks processed: {len(my_dicts)}")

# #============================================================================================================================================================================


# import requests 
# import os
# import json
# import pandas as pd

# def create_embedding(text_list):
#     r = requests.post("http://localhost:11434/api/embed",json={
#         "model":"bge-m3",
#         "input":text_list
#     })

#     embedding = r.json()['embeddings']
#     return embedding

# jsons = os.listdir("jsons")
# my_dicts = []
# chunk_id = 0

# for json_file in jsons:
#     with open(f"jsons/{json_file}") as f:
#         content = json.load(f)
#     embeddings = create_embedding([c['text'] for c in content['chunks']])

#     for i, chunk in enumerate(content['chunks']):
#         chunk['chunk_id'] = chunk_id
#         chunk['embedding'] = embeddings[i]
#         chunk_id += 1
#         my_dicts.append(chunk)
#         print(chunk)
#     break
# # print(my_dicts)

# df = pd.DataFrame.from_records(my_dicts)
# print(df)


import requests
import os
import json
import numpy as np
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
import joblib

def create_embedding(text_list):
    # https://github.com/ollama/ollama/blob/main/docs/api.md#generate-embeddings
    r = requests.post("http://localhost:11434/api/embed", json={
        "model": "bge-m3",
        "input": text_list
    })

    embedding = r.json()["embeddings"] 
    return embedding


jsons = os.listdir("jsons")  # List all the jsons 
my_dicts = []
chunk_id = 0

for json_file in jsons:
    with open(f"jsons/{json_file}") as f:
        content = json.load(f)
    print(f"Creating Embeddings for {json_file}")
    embeddings = create_embedding([c['text'] for c in content['chunks']])
       
    for i, chunk in enumerate(content['chunks']):
        chunk['chunk_id'] = chunk_id
        chunk['embedding'] = embeddings[i]
        chunk_id += 1
        my_dicts.append(chunk) 
# print(my_dicts)

df = pd.DataFrame.from_records(my_dicts)
# Save this dataframe 
joblib.dump(df, 'embeddings.joblib')  

