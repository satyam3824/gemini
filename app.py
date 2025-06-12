
import streamlit as st
import google.generativeai as genai

import os
import hmac

def check_password():
    """Returns `True` if the user had a correct password."""

    def login_form():
        """Form with widgets to collect user information"""
        with st.form("Credentials"):
            st.text_input("Username", key="username")
            st.text_input("Password", type="password", key="password")
            st.form_submit_button("Log in", on_click=password_entered)

    def password_entered():
        """Checks whether a password entered by the user is correct."""
        if st.session_state["username"] in st.secrets[
            "passwords"
        ] and hmac.compare_digest(
            st.session_state["password"],
            st.secrets.passwords[st.session_state["username"]],
        ):
            st.session_state["password_correct"] = True
            del st.session_state["password"]  # Don't store the username or password.
            del st.session_state["username"]
        else:
            st.session_state["password_correct"] = False

    # Return True if the username + password is validated.
    if st.session_state.get("password_correct", False):
        return True

    # Show inputs for username + password.
    login_form()
    if "password_correct" in st.session_state:
        st.error("😕 User not known or password incorrect")
    return False


if not check_password():
    st.stop()
from google import genai
    

#REF: https://ai.google.dev/gemini-api/docs/text-generation?authuser=3&lang=python
client = genai.client(api_key=st.secrets["api_key"]["api_key"]) #API KEY

#model = genai.GenerativeModel("gemini-2.0-flash") #MODEL NAME AND VERSION




#main application starts
def grammar_check(text):
    """
    A placeholder function for grammar checking.
    """
    if not text.strip():
        return "Please enter text."
    
    response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents=[f"generate a grammatically sound English sentence from the given information : {text}."] 

        
    '''
    PROMPT : Input to generate model response
    '''
   # print(response.text) #OUTPUT OF THE MODEL


    # This is where your actual grammar checking logic would go.
    # For now, it just shows a placeholder result.
    checked_text = f"Original: {text}\n\nResult: {response.text}"
    
    return checked_text

st.set_page_config(page_title="Grammar Check", layout="centered")

st.title("Grammar Checker")
st.write("Type your text below and click 'Check' to get suggestions.")

user_input = st.text_area(
    "Your Text:",
    height=200,
    placeholder="Enter text here..."
)

if st.button("Check"):
    if user_input:
        result = grammar_check(user_input)
        st.subheader("Result:")
        st.markdown(result)
    else:
        st.warning("Please enter some text.")

st.markdown("---")
st.caption("Simple Grammar Checker")
