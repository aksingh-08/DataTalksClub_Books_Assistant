import streamlit as st

def show_answer(result):
    with st.container(border=True):
        st.subheader('Answer')
        st.write(result.answer)

def show_sources(result):
    st.subheader('Books Used')
    for source in result.sources:
        st.write(f"• {source} ")

def show_metadata(result):
    st.subheader('Metadata')
    c1, c2 = st.columns(2)
    with c1:
        st.metric('Model', result.model)
        st.metric('Retriever', result.retriever)
    with c2:
        st.metric(
            'Response Time',
            f'{result.response_time:.2f}s'
        )
        st.metric(
            'Prompt Tokens',
            result.prompt_tokens
        )
        st.metric(
            'Completion Tokens',
            result.completion_tokens
        )
        st.metric(
            'Total Tokens',
            result.total_tokens
        )

def show_retrieved_documents(result):
    with st.expander('Retrieved Documents'):
        for doc in result.documents:
            st.subheader(doc['book_title'])
            with st.expander('View full document'):
                st.write(doc['search_text'])
            st.divider()
            