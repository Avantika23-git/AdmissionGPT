from predictor import recommend_branches
from cutoff_analyzer import analyze_cutoff
from faq_engine import search_faq
from parser import extract_rank_category

def chat(user_message):

    rank, category = extract_rank_category(
        user_message
    )

    if rank is not None and category is not None:

        return {
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

    faq_answer = search_faq(
        user_message
    )

    if faq_answer:
        return faq_answer

    return (
        "Please provide your KEAM rank "
        "and category."
    )
while True:

    message = input(
        "\nYou : "
    )

    result = chat(
        message
    )

    print("\nAdmissionGPT :")
    print(result)