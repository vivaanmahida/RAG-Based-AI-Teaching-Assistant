# def create_embedding(text_list):

#     r = requests.post("http://localhost:11434/api/embed",json={
#         "model": "bge-m3",
#         "input": text_list
#     })

#     embedding = r.json()["embedding"]
#     return embedding

#--------------------------------------------------------------------------------------------------------------------------

# def create_embedding(text_list):
#     r = requests.post(
#         "http://localhost:11434/api/embed",
#         json={
#             "model": "bge-m3",
#             "input": text_list
#         }
#     )
#     return r.json()["embedding"]

#---------------------------------------------------------------------------------------------------------------------------
# def create_embedding(text):
#     r = requests.post(
#         "http://localhost:11434/api/embed",
#         json={
#             "model": "bge-m3",
#             "input": text
#         }
#     )

#     data = r.json()

#     if "embedding" in data:
#         return data["embedding"]
#     elif "embeddings" in data:
#         return data["embeddings"][0]
#     else:
#         raise ValueError(f"Unexpected response: {data}")



# jsons = os.listdir("jsons")
# my_dicts = []
# chunk_id = 0

# for json_file in jsons:
#     with open(f"jsons/{json_file}") as f:
#         content = json.load(f)
#     print(f"Creating Embedding for {json_file}")
#     embeddings = create_embedding([c['text']for c in content['chunks']])

#     for i,chunk in enumerate(content['chunks']):
#         chunk['chunk_id'] = chunk_id
#         chunk['embedding'] = embeddings[i]
#         chunk_id += 1
#         my_dicts.append(chunk)

# df = pd.DataFrame.from_records(my_dicts)
# print(df)

# def create(text):
#     r = requests.post("http://localhost:11434/api/embeddings",json={
#         "model": "bge-m3",
#         "prompt":text
#     })

#     embedding = r.json()['embedding']
#     return embedding

# a = create("Vivaan is good boi")
# print(a)