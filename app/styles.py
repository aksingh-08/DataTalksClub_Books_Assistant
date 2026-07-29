import streamlit as st

def load_css():
    st.markdown(
        '''
        <style>
        .block-container{
            max-width:1100px;
            padding-top:2rem;
            padding-bottom:2rem;
        }
        </style>
        ''',
        unsafe_allow_html=True
    )