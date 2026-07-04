import streamlit as st


def load_css():

    st.markdown("""

<style>

html,
body,
[class*="css"]{

    font-family:Arial;

}

.main{

    background:#f5f7fa;

}

.block-container{

    padding-top:1.5rem;
    padding-bottom:1rem;

}

h1{

    color:#00695c;

}

.stChatMessage{

    border-radius:15px;

}

.stButton>button{

    width:100%;
    border-radius:10px;
    border:none;
    background:#0F766E;
    color:white;

}

.stButton>button:hover{

    background:#115e59;
    color:white;

}

footer{

visibility:hidden;

}

</style>

""",unsafe_allow_html=True)