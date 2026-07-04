import streamlit as st


def show_predictions(df):

    st.subheader("🏆 Recommended Branches")

    for _,row in df.iterrows():

        probability=float(row["Probability"])

        st.write(f"### {row['Course']}")

        st.progress(probability/100)

        st.caption(f"{probability:.2f}% Confidence")