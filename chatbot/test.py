"""from predictor import recommend_branches

print(
    recommend_branches(
        3500,
        "GN"
    )
)"""

"""from cutoff_analyzer import analyze_cutoff

print(
    analyze_cutoff(
        3500,
        "GN"
    )
)"""
from llm_handler import ask_llm

reply = ask_llm(
    "Say hello in one sentence."
)

print(reply)