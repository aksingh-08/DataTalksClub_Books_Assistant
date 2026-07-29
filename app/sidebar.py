import streamlit as st
from rag.config import(MODEL_NAME, SEARCH_METHOD)

def render_sidebar():
    with st.sidebar:
        st.title('Books Assistant')
        st.divider()
        st.subheader('Configuration')
        st.write(f'Model: {MODEL_NAME}')
        st.write(f'Retriever: {SEARCH_METHOD}')
        st.divider()
        st.info(
            'Ask questions about the DataTalksClub'
            'Book of the Week archive.'
        )