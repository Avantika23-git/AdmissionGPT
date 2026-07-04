import pandas as pd

import chromadb

from sentence_transformers import SentenceTransformer

# --------------------------
# Load Embedding Model
# --------------------------

model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)

# --------------------------
# Read FAQ Excel
# --------------------------

faq = pd.read_excel(
    "data/faq.xlsx"
)

# --------------------------
# Connect to ChromaDB
# --------------------------

client = chromadb.PersistentClient(
    path="vector_db/chroma"
)

# --------------------------
# Delete Old Collection
# --------------------------

try:
    client.delete_collection(
        "faq"
    )
except:
    pass

# --------------------------
# Create Fresh Collection
# --------------------------

collection = client.create_collection(
    name="faq"
)

# --------------------------
# Store Every FAQ
# --------------------------

for index, row in faq.iterrows():

    embedding = model.encode(
        row["Question"]
    ).tolist()

    collection.add(

        ids=[
            str(index)
        ],

        documents=[
            row["Question"]
        ],

        embeddings=[
            embedding
        ],

        metadatas=[

            {

                "answer":
                row["Answer"]

            }

        ]

    )

print(
    "Vector Database Created Successfully!"
)