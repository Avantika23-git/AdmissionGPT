import streamlit as st


def initialize_chat():

    if "messages" not in st.session_state:

        st.session_state.messages=[]


def show_history():

    for message in st.session_state.messages:

        with st.chat_message(message["role"]):

            st.write(message["content"])


def add_message(role,text):

    st.session_state.messages.append(

        {

            "role":role,

            "content":text

        }

    )