import streamlit as st


def show_cutoffs(df):

    st.subheader("📊 Historical Cutoff Analysis")

    display=df.copy()

    def color(chance):

        if chance=="Very High Chance":

            return "🟢 Very High"

        elif chance=="High Chance":

            return "🟢 High"

        elif chance=="Possible":

            return "🟡 Possible"

        else:

            return "🔴 Low"

    display["Chance"]=display["Chance"].apply(color)

    st.dataframe(

        display,

        hide_index=True,

        use_container_width=True

    )