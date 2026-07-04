import streamlit as st


def show_sidebar():

    with st.sidebar:

        st.title("🎓 AdmissionGPT")

        st.caption(
            "Government Model Engineering College"
        )

        st.divider()

        st.subheader("Features")

        st.write("🎯 Branch Prediction")

        st.write("📊 Cutoff Analysis")

        st.write("📚 FAQ Search")

        st.write("🤖 AI Chat")

        st.divider()

        st.subheader("Quick Questions")

        questions=[

            "What is CSBS?",

            "Seat Intake",

            "Fee Structure",

            "Required Documents",

            "Eligibility",

            "What is ECE?",

            "Mechanical Engineering",

            "Can AdmissionGPT guarantee admission?",

            "Hostel Facilities",

            "Placements"

        ]

        for q in questions:

            if st.button(q):

                st.session_state.prompt=q