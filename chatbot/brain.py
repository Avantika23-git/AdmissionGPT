from chatbot.router import detect_intent
from chatbot.parser import extract_rank_category
from chatbot.predictor import recommend_branches
from chatbot.cutoff_analyzer import analyze_cutoff
from chatbot.rag import retrieve_context
from chatbot.llm_handler import ask_llm


def chat(user_message):

    intent = detect_intent(
        user_message
    )

    # ------------------------

    if intent == "prediction":

        rank, category = extract_rank_category(
            user_message
        )

        return {

            "type":"prediction",

            "branches":

            recommend_branches(
                rank,
                category
            ),

            "cutoffs":

            analyze_cutoff(
                rank,
                category
            )

        }

    # ------------------------

    if intent == "rag":

        docs = retrieve_context(
            user_message
        )

        context = ""

        for doc in docs:

            context += f"""

Question:

{doc['Question']}

Answer:

{doc['Answer']}

"""

        answer = ask_llm(

            user_message,

            context

        )

        return {

            "type":"rag",

            "answer":answer

        }

    # ------------------------

    if intent == "general":

        answer = ask_llm(

            user_message,

            "No admission context."

        )

        return {

            "type":"general",

            "answer":answer

        }