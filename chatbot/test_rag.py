from rag import retrieve_context

results = retrieve_context(
    "wht is placement"
)

for i, item in enumerate(results, start=1):

    print("="*50)

    print(
        "Result",
        i
    )

    print()

    print(
        "Question :",
        item["Question"]
    )

    print()

    print(
        "Answer :",
        item["Answer"]
    )

    print()

    print(
        "Distance :",
        item["Distance"]
    )