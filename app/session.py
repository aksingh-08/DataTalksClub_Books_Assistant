import streamlit as st

def initialize_session():
    if 'history' not in st.session_state:
        st.session_state.history = []
    if 'current_response' not in st.session_state:
        st.session_state.current_response = None