import streamlit as st

from chatbot.parser import extract_rank_category
from chatbot.predictor import recommend_branches
from chatbot.cutoff_analyzer import analyze_cutoff
from chatbot.faq_engine import search_faq


st.set_page_config(
    page_title="AdmissionGPT",
    page_icon="🎓",
    layout="wide"
)


st.title("🎓 AdmissionGPT")
st.subheader(
    "MEC Admission Assistant"
)

st.write(
    """
    Ask questions about MEC admissions
    or enter your KEAM Rank and Category.
    """
)


user_input = st.text_input(
    "Enter your query"
)


if st.button("Submit"):

    if user_input:

        faq_answer = search_faq(
            user_input
        )

        if faq_answer:

            st.success(
                faq_answer
            )

        else:

            rank, category = extract_rank_category(
                user_input
            )

            if rank and category:

                st.success(
                    f"Detected Rank: {rank} | Category: {category}"
                )

                branches = recommend_branches(
                    rank,
                    category
                )

                cutoffs = analyze_cutoff(
                    rank,
                    category
                )

                st.subheader(
                    "Recommended Branches"
                )

                st.dataframe(
                    branches,
                    use_container_width=True
                )

                st.subheader(
                    "Admission Chances"
                )

                st.dataframe(
                    cutoffs,
                    use_container_width=True
                )

            else:

                st.warning(
                    "Please provide a valid KEAM rank and category."
                )
    # =====================================
# POPULAR FAQs
# =====================================

st.subheader("📌 Popular Questions")

with st.expander("What is CSBS?"):
    st.write(
        "Computer Science and Business Systems combines Computer Science with Business and Management subjects."
    )

with st.expander("What is CSE?"):
    st.write(
        "Computer Science and Engineering focuses on programming, software development, AI, data structures and computer systems."
    )

with st.expander("What is ECE?"):
    st.write(
        "Electronics and Communication Engineering deals with communication systems, embedded systems and electronics."
    )

with st.expander("What is EEE?"):
    st.write(
        "Electrical and Electronics Engineering focuses on power systems, electrical machines and electronics."
    )

with st.expander("What is VLSI?"):
    st.write(
        "VLSI Engineering focuses on chip design, semiconductor technology and integrated circuits."
    )

with st.expander("What is MEC?"):
    st.write(
        "Government Model Engineering College (MEC), Thrikkakara, is one of Kerala's leading engineering colleges."
    )

with st.expander("Who conducts KEAM?"):
    st.write(
        "KEAM is conducted by the Commissioner for Entrance Examinations (CEE), Kerala."
    )

with st.expander("Which branch has the highest cutoff in MEC?"):
    st.write(
        "Computer Science and Engineering usually has the highest cutoff rank."
    )

with st.expander("Which branch has the best placements?"):
    st.write(
        "CSE and CSBS generally record the highest placement statistics, followed by ECE."
    )

with st.expander("What can AdmissionGPT do?"):
    st.write(
        "AdmissionGPT predicts branch preferences, analyzes admission chances using cutoff trends, and answers MEC admission related questions."
    )