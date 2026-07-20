# pages_content.py
import streamlit as st
import pandas as pd
from data import HEALTH_DATABASE
from data import SUBSTANCE_DATABASE


def render_home():
    st.title("Welcome to the Health Index")
    st.write(
        "Your all-in-one dashboard connecting lifestyle habits, nutrition, and disease prevention.")
    st.markdown("---")
    st.write("Use the navigation menu at the top to explore the **Health Index** database or read our **FAQ**.")


def render_index():
    st.title("The Health Index")
    st.write("A clean, evidence-based dashboard connecting diseases to lifestyle levers and dietary choices.")

    st.caption("**Disclaimer:** This website is for informational purposes only. It is not a substitute for professional medical advice.")
    st.markdown("---")

    all_diseases = list(HEALTH_DATABASE.keys())
    selected_disease = st.selectbox(
        "Select a condition to research:", all_diseases)

    if selected_disease:
        data = HEALTH_DATABASE[selected_disease]
        st.header(selected_disease)
        st.write(f"**{data['summary']}**")
        st.markdown("---")

        st.subheader("Nutrients")
        for lever in data["nutrients"]:
            st.markdown(f"**• {lever['factor']}**")
            st.write(lever['impact'])

        st.markdown("---")
        st.subheader("Actions")
        for lever in data["actions"]:
            st.markdown(f"**• {lever['factor']}**")
            st.write(lever['impact'])

        st.markdown("---")
        st.subheader("Risks")
        for lever in data["risks"]:
            st.markdown(f"**• {lever['factor']}**")
            st.write(lever['impact'])


def render_faq():
    st.title("Frequently Asked Questions")
    st.markdown("---")

    with st.expander("What is the goal of this website?"):
        st.write("This site centralizes spread-out public health data into a simple, scannable dashboard linking diseases to specific foods and lifestyle habits.")

    with st.expander("Where does this data come from?"):
        st.write("All data is curated from trusted institutional public guidelines, such as the NIH, Mayo Clinic, and major disease advocacy associations.")


def render_substances():
    st.title("Substances and their effects")

    all_substances = list(SUBSTANCE_DATABASE.keys())
    selected_substance = st.selectbox(
        "Select a substance to research:", all_substances)

    if selected_substance:
        data = SUBSTANCE_DATABASE[selected_substance]

        st.header(selected_substance)
        st.write(f"**{data['summary']}**")
        st.markdown("---")

        st.subheader("Benefits")
        for lever in data["nutrients"]:
            st.markdown(f"**• {lever['factor']}**")
            st.write(lever['impact'])

        st.markdown("---")
        st.subheader("Risks")
        for lever in data["actions"]:
            st.markdown(f"**• {lever['factor']}**")
            st.write(lever['impact'])
