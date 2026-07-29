import streamlit as st

from monitoring.feedback import save_feedback, get_feedback

# def render_feedback(conversation_id: int):
    # if 'feedback_given' not in st.session_state:
    #     st.session_state.feedback_given = {}
    # if conversation_id in st.session_state.feedback_given:
    #     rating = st.session_state.feedback_given[conversation_id]
    #     if rating == 'helpful':
    #         st.success('You marked this response as Helpful.')
    #     elif rating == 'Not Helpful':
    #         st.warning('You marked this response as Not Helpful.')
    #     return
    # st.caption('Was this answer helpful?')

    # col1, col2 = st.columns(2)
    # with col1:
    #     if st.button('Helpful', key=f'helpful_{conversation_id}', use_container_width=True):
    #         save_feedback(conversation_id, 'Helpful')
    #         st.session_state.feedback_given[conversation_id] = 'Helpful'
    #         st.rerun()
    # with col2:
    #     if st.button('Not Helpful', key=f'not_helpful_{conversation_id}', use_container_width=True):
    #         save_feedback(conversation_id, 'Not Helpful')
    #         st.session_state.feedback_given[conversation_id] = 'Not Helpful'
    #         st.rerun()

def render_feedback(conversation_id: int):
    current_feedback = get_feedback(conversation_id)
    if current_feedback == 'Helpful':
        st.success('You marked this response as Helpful.')
        return
    if current_feedback == 'Not Helpful':
        st.warning('You marked this response as Not Helpful.')
        return
    st.caption('Was this answer helpful?')

    col1, col2 = st.columns(2)
    with col1:
        if st.button('Helpful', key=f'helpful_{conversation_id}'):
            save_feedback(conversation_id, 'Helpful')
            st.rerun()
    with col2:
        if st.button('Not Helpful', key=f'not_helpful_{conversation_id}'):
            save_feedback(conversation_id, 'Not Helpful')
            st.rerun()