import streamlit as st
import pandas as pd

from chatbot.brain import chat

# -----------------------------------
# PAGE CONFIG
# -----------------------------------

st.set_page_config(
    page_title="AdmissionGPT",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -----------------------------------
# CUSTOM CSS
# -----------------------------------

st.markdown("""
<style>

.block-container{
    padding-top:2rem;
}

h1{
    color:#0F766E;
}

.stChatMessage{
    border-radius:15px;
}

</style>
""", unsafe_allow_html=True)

# -----------------------------------
# SIDEBAR
# -----------------------------------

with st.sidebar:

    st.title("🎓 AdmissionGPT")

    st.caption(
        "Government Model Engineering College"
    )

    st.divider()

    st.subheader("What can I do?")

    st.write("✅ Branch Prediction")

    st.write("✅ Historical Cutoff Analysis")

    st.write("✅ Admission FAQ")

    st.write("✅ AI Chat")

    st.divider()

    st.subheader("Quick Questions")

    quick_questions = [

        "What is CSBS?",

        "How many seats are available in CSE?",

        "What documents are required?",

        "What is the fee structure?",

        "Who is eligible for KEAM?",

        "Can AdmissionGPT guarantee admission?",

        "How is cutoff decided?",

        "What is ECE?",

        "Tell me about Mechanical Engineering.",

        "What can you do?"

    ]

    for q in quick_questions:

        if st.button(q):

            st.session_state.quick_prompt = q

# -----------------------------------
# HEADER
# -----------------------------------

st.title("🎓 AdmissionGPT")

st.caption(
    "AI-powered Admission Assistant for Government Model Engineering College"
)

# -----------------------------------
# WELCOME MESSAGE
# -----------------------------------

if "messages" not in st.session_state:

    st.session_state.messages=[]

if len(st.session_state.messages)==0:

    st.info("""

👋 Welcome to AdmissionGPT!

You can ask things like:

• My rank is 3500 and category GN

• Suggest branches for rank 6000 ST

• What is CSBS?

• How many seats are available in CSE?

• Required documents

""")

# -----------------------------------
# DISPLAY CHAT HISTORY
# -----------------------------------

for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        if message["role"]=="assistant":

            if isinstance(message["content"],dict):

                if "branches" in message["content"]:

                    st.subheader("🏆 Top Branch Predictions")

                    branches=message["content"]["branches"]

                    for _,row in branches.iterrows():

                        st.metric(

                            label=row["Course"],

                            value=f"{row['Probability']:.2f}%"

                        )

                if "cutoffs" in message["content"]:

                    st.subheader("📊 Historical Cutoff Analysis")

                    st.dataframe(

                        message["content"]["cutoffs"],

                        hide_index=True,

                        use_container_width=True

                    )

            else:

                st.write(message["content"])

        else:

            st.write(message["content"])

# -----------------------------------
# INPUT
# -----------------------------------

prompt = st.chat_input(
    "Ask anything about MEC admissions..."
)

# Quick Question clicked?

if "quick_prompt" in st.session_state:

    prompt=st.session_state.quick_prompt

    del st.session_state.quick_prompt

# -----------------------------------
# CHAT
# -----------------------------------

if prompt:

    st.session_state.messages.append(

        {

            "role":"user",

            "content":prompt

        }

    )

    with st.chat_message("user"):

        st.write(prompt)

    with st.spinner("Thinking..."):

        result=chat(prompt)

    with st.chat_message("assistant"):

        if result["type"]=="prediction":

            branches=result["branches"]

            cutoffs=result["cutoffs"]

            st.success("Prediction completed successfully.")

            st.subheader("🏆 Top Branch Predictions")

            for _,row in branches.iterrows():

                st.metric(

                    label=row["Course"],

                    value=f"{row['Probability']:.2f}%"

                )

            st.subheader("📊 Historical Cutoff Analysis")

            st.dataframe(

                cutoffs,

                hide_index=True,

                use_container_width=True

            )

            assistant_message={

                "branches":branches,

                "cutoffs":cutoffs

            }

        else:

            st.write(result["answer"])

            assistant_message=result["answer"]

    st.session_state.messages.append(

        {

            "role":"assistant",

            "content":assistant_message

        }

    )

# -----------------------------------
# FOOTER
# -----------------------------------

st.divider()

st.caption(
    "Developed using Machine Learning • ChromaDB • Gemini • Streamlit"
)