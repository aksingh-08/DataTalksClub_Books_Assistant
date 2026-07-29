import streamlit as st

from rag.pipeline import RAGPipeline
from app.components import (
    show_answer,
    show_metadata,
    show_sources,
    show_retrieved_documents
)

from app.sidebar import render_sidebar
from app.session import initialize_session
from app.styles import load_css

st.set_page_config(
    page_title='DataTalkClub Books Assistant',
    layout='wide'
)
load_css()
initialize_session()
render_sidebar()
rag = RAGPipeline()
st.title('DataTalksClub Books Assistant')
st.write(
    'Ask questions about the'
    'DataTalksClub Book of the Week archive.'
)

for message in st.session_state.messages:
    if message['role'] == 'user':
        with st.chat_message('user'):
            st.write(message['content'])
    else:
        result = message['result']
        with st.chat_message('assistant'):
            show_answer(result)
            with st.expander('Details'):
                show_sources(result)
                st.divider()
                show_metadata(result)
                st.divider()
                show_retrieved_documents(result)

question = st.chat_input(
    'Ask about the DataTalksClub books...',
    # placeholder='e.g. What is Data Engineering?',
)

# if st.button('Ask'):
#     if question.strip():
#         with st.spinner('Searching books...'):
#             result = rag.ask(question)
#         st.session_state.current_response = result
#         st.session_state.history.append(result)
#     if st.session_state.current_response:
#         result = st.session_state.current_response
#         show_answer(result)
#         st.divider()
#         show_sources(result)
#         st.divider()
#         show_metadata(result)
#         st.divider()
#         show_retrieved_documents(result)

if question:
    st.session_state.messages.append(
        {
            'role': 'user',
            'content': question
        }
    )
    with st.chat_message('user'):
        st.write(question)
    with st.chat_message('assistant'):
        with st.spinner('Searching books...'):
            result = rag.ask(question)
        show_answer(result)
        with st.expander('Details'):
            show_sources(result)
            st.divider()
            show_metadata(result)
            st.divider()
            show_retrieved_documents(result)
    st.session_state.messages.append(
        {
            'role': 'assistant',
            'result': result
        }
    )