import streamlit as st
import pandas as pd

from monitoring.database import initialize_database
from monitoring.analytics import (
    get_total_queries,
    get_average_latency,
    get_average_tokens,
    get_recent_queries,
    get_feedback_stats,
    get_latency_history,
    get_token_history,
    get_top_books,
)

initialize_database()

st.set_page_config(
    page_title="Analytics Dashboard",
    layout="wide",
)

st.title("Analytics Dashboard")
c1, c2, c3 = st.columns(3)
with c1:
    st.metric(
        "Total Queries",
        get_total_queries(),
    )
with c2:
    st.metric(
        "Average Latency",
        f"{get_average_latency():.2f}s",
    )
with c3:
    st.metric(
        "Average Tokens",
        f"{get_average_tokens():.0f}",
    )
st.divider()
st.subheader("Latency Trend")
latency = get_latency_history()
if latency:
    st.line_chart(pd.DataFrame(latency, columns=["Latency"]))
else:
    st.info("No data available.")
st.divider()
st.subheader("Token Usage")
tokens = get_token_history()
if tokens:
    st.line_chart(pd.DataFrame(tokens, columns=["Tokens"]))
else:
    st.info("No data available.")
st.divider()
st.subheader("Feedback")
feedback = get_feedback_stats()
if feedback:
    df = pd.DataFrame(
        feedback,
        columns=["Rating", "Count"],
    )
    st.bar_chart(
        df.set_index("Rating")
    )
else:
    st.info("No feedback yet.")
st.divider()
st.subheader("Most Referenced Books")
books = get_top_books()
if books:
    df = pd.DataFrame(
        books,
        columns=["Book", "Count"],
    )
    st.bar_chart(
        df.set_index("Book")
    )
else:
    st.info("No book statistics yet.")
st.divider()
st.subheader("Recent Queries")
queries = get_recent_queries()
if queries:
    df = pd.DataFrame(
        queries,
        columns=[
            "Question",
            "Latency",
            "Tokens",
            "Time",
        ],
    )
    st.dataframe(
        df,
        use_container_width=True,
    )
else:
    st.info("No queries yet.")
    