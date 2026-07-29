import streamlit as st
def load_css():
    st.markdown(
        '''
        <style>
        .block-container{
            padding-top:2rem;
            padding-bottom:2rem;
            max-width:1100px;
        }
        </style>
        ''',
        unsafe_allow_html=True
    )