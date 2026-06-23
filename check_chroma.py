import chromadb

client = chromadb.PersistentClient(
    path="data/chroma"
)

collection = client.get_collection(
    "video_4RVGipmXvHs"
)

print("Count:", collection.count())

data = collection.peek(limit=3)

print(data)