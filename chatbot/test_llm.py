from rag import retrieve_context

from llm_handler import ask_llm

question = "whats up"

results = retrieve_context(question)

context = ""

for item in results:

    context += f"""
Question:
{item['Question']}

Answer:
{item['Answer']}

----------------------------

"""

answer = ask_llm(
    question,
    context
)

print(answer)