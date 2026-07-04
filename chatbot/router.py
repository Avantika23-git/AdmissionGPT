from chatbot.parser import extract_rank_category
from chatbot.rag import retrieve_context


def detect_intent(message):

    rank, category = extract_rank_category(
        message
    )

    if rank is not None and category is not None:

        return "prediction"

    results = retrieve_context(message, n_results=1)

    if results and results[0]["Distance"] < 1.3:
        return "rag"

    return "general"