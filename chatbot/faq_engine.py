import pandas as pd

faq_df = pd.read_excel(
    "data/faq.xlsx"
)
def search_faq(question):

    question = question.lower()

    for _, row in faq_df.iterrows():

        if row["Question"].lower() in question:

            return row["Answer"]

    return None

"""print(search_faq(
    "What is CSBS?"
))"""