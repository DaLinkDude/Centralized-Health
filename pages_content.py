# pages_content.py
import streamlit as st
import pandas as pd
from data import HEALTH_DATABASE


def render_home():
    st.title("🏡 Welcome to the Centralized Health Index")
    st.write(
        "Your all-in-one dashboard connecting lifestyle habits, nutrition, and disease prevention.")
    st.markdown("---")
    st.write("Use the navigation menu at the top to explore the **Health Index** database or read our **FAQ**.")


def render_index():
    st.title("🍏 The Centralized Health Index")
    st.write("A clean, evidence-based dashboard connecting diseases to lifestyle levers and dietary choices.")

    st.caption("⚠️ **Disclaimer:** This website is for informational purposes only. It is not a substitute for professional medical advice.")
    st.markdown("---")

    all_diseases = list(HEALTH_DATABASE.keys())
    selected_disease = st.selectbox(
        "Select a condition to research:", all_diseases)

    if selected_disease:
        data = HEALTH_DATABASE[selected_disease]
        st.header(selected_disease)
        st.write(f"*{data['summary']}*")
        st.markdown("---")

        st.subheader("🔑 Top Lifestyle & Nutrient Levers")
        for lever in data["levers"]:
            st.markdown(f"**• {lever['factor']}**")
            st.write(lever['impact'])
            st.write("")

        st.markdown("---")
        st.subheader("🛒 Recommended Grocery Items")
        food_df = pd.DataFrame(data["foods"]).set_index("Food")
        st.dataframe(food_df, width=None)


def render_faq():
    st.title("🙋 Frequently Asked Questions")
    st.markdown("---")

    with st.expander("What is the goal of this website?"):
        st.write("This site centralizes spread-out public health data into a simple, scannable dashboard linking diseases to specific foods and lifestyle habits.")

    with st.expander("Where does this data come from?"):
        st.write("All data is curated from trusted institutional public guidelines, such as the NIH, Mayo Clinic, and major disease advocacy associations.")
