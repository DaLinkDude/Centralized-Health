# app.py
# cd health-index-app
# streamlit run app.py
# or c:/Users/Willi/.vscode/Health-App-Index/app.py
import streamlit as st
from pages_content import render_home, render_index, render_faq, render_substances

# 1. Base Configuration
st.set_page_config(page_title="Centralized Health Index",
                   page_icon="🍏", layout="centered")

# 2. Classic Sidebar Selectbox Navigation
st.sidebar.title("Navigation")
page_choice = st.sidebar.radio(
    "Go to:", ["Home", "Health Index", "FAQ", "Substances"])

# 3. Router Logic (Manually loading the functions based on user click)
if page_choice == "Home":
    render_home()
elif page_choice == "Health Index":
    render_index()
elif page_choice == "FAQ":
    render_faq()
elif page_choice == "Substances":
    render_substances()
