import chromadb

from sentence_transformers import SentenceTransformer

model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)

client = chromadb.PersistentClient(
    path="vector_db/chroma"
)

collection = client.get_collection(
    "faq"
)


def retrieve_context(
    query,
    n_results=5,
    threshold=1.30
):

    embedding = model.encode(
        query
    ).tolist()

    results = collection.query(

        query_embeddings=[
            embedding
        ],

        n_results=n_results

    )

    final_results = []

    documents = results["documents"][0]

    metadatas = results["metadatas"][0]

    distances = results["distances"][0]

    for doc, meta, distance in zip(
        documents,
        metadatas,
        distances
    ):

        if distance <= threshold:

            final_results.append(

                {

                    "Question": doc,

                    "Answer": meta["answer"],

                    "Distance": distance

                }

            )

    return final_results