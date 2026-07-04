import os
import google.generativeai as genai
from dotenv import load_dotenv

# 1. Load environment variables and configure Gemini
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# 2. Initialize the model
model = genai.GenerativeModel("gemini-2.5-flash")

# 3. Define the AI response function
def ask_llm(question, context=""):
    # Strip any accidental spaces from the context
    context = context.strip()

    # Case A: Handling Chit-Chat / Greetings (No document context passed)
    if context == "No admission context." or context == "":
        prompt = f"""
You are AdmissionGPT.
You are a friendly AI assistant for Government Model Engineering College.

Answer naturally.
- If someone greets you, greet them.
- If someone thanks you, respond politely.
- If someone asks what you do, explain that you help students with KEAM admissions.

Question:
{question}
"""

    # Case B: Handling actual RAG answers (Document context is found)
    else:
        prompt = f"""
You are AdmissionGPT.
You answer ONLY using the retrieved admission information below.

Rules:
1. Never make up information.
2. If multiple pieces of information are relevant, include ALL of them.
3. Do NOT summarize important facts.
4. Mention numbers like seat intake, cutoff, dates, and fees whenever available.
5. If the answer is not available in the text, say: 'I couldn't find that information in the admission documents.'

Retrieved Information:
{context}

Student Question:
{question}

Answer:
"""

    # 4. Send the correct prompt to Gemini and return the response
    response = model.generate_content(prompt)
    return response.text
