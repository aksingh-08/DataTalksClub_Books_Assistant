from pathlib import Path

import pandas as pd
import streamlit as st

RESULTS_FILE = (
    Path(__file__).parent.parent
    / "evaluation"
    / "results"
    / "evaluation_results.csv"
)

st.set_page_config(
    page_title="Evaluation Dashboard",
    layout="wide",
)

st.title("RAG Evaluation Dashboard")

if not RESULTS_FILE.exists():
    st.warning(
        "No evaluation report found.\n\n"
        "Run:\n\n"
        "python run_evaluation.py"
    )
    st.stop()

df = pd.read_csv(RESULTS_FILE)

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Questions",
        len(df),
    )

with col2:
    st.metric(
        "Average Precision",
        f"{df['precision'].mean():.2f}",
    )

with col3:
    st.metric(
        "Average Recall",
        f"{df['recall'].mean():.2f}",
    )

col4, col5, col6 = st.columns(3)

with col4:
    st.metric(
        "Average F1",
        f"{df['f1'].mean():.2f}",
    )

with col5:
    st.metric(
        "Average Response Time",
        f"{df['response_time'].mean():.2f} s",
    )

with col6:
    st.metric(
        "Average Tokens",
        f"{df['total_tokens'].mean():.0f}",
    )

st.divider()

st.subheader("Retrieval Metrics")

st.line_chart(
    df[["precision", "recall", "f1"]]
)

st.divider()

st.subheader("Response Time")

st.line_chart(
    df["response_time"]
)

st.divider()

st.subheader("Token Usage")

st.bar_chart(
    df["total_tokens"]
)

st.divider()

st.subheader("Evaluation Results")

st.dataframe(
    df,
    use_container_width=True,
)
st.divider()
st.metric(
    "Average Answer Overlap",
    f"{df['answer_overlap'].mean():.2f}",
)