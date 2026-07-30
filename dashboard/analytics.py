import pandas as pd

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


def load_dashboard_data():

    return {

        "total_queries": get_total_queries(),

        "avg_latency": get_average_latency(),

        "avg_tokens": get_average_tokens(),

        "feedback": get_feedback_stats(),

        "latency": get_latency_history(),

        "tokens": get_token_history(),

        "books": get_top_books(),

        "queries": pd.DataFrame(

            get_recent_queries(),

            columns=[
                "Question",
                "Latency",
                "Tokens",
                "Timestamp",
            ],
        ),
    }