import streamlit as st

from monitoring.database import initialize_database
from monitoring.conversation import save_conversation
from monitoring.schema import ConversationLog

from app.feedback_component import render_feedback

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
initialize_database()
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
            if hasattr(result, 'conversation_id'):
                render_feedback(result.conversation_id)
            with st.expander('Details'):
                show_sources(result)
                st.divider()
                show_metadata(result)
                st.divider()
                show_retrieved_documents(result)

question = st.chat_input(
    'Ask about the DataTalksClub books...',
)

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
        conversation_id = save_conversation(
            ConversationLog(
                question=result.question,
                answer=result.answer,
                model=result.model,
                retriever=result.retriever,
                sources=result.sources,
                prompt_tokens=result.prompt_tokens,
                completion_tokens=result.completion_tokens,
                total_tokens=result.total_tokens,
                response_time=result.response_time,
            )
        )
        result.conversation_id = conversation_id
        show_answer(result)
        render_feedback(result.conversation_id)
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