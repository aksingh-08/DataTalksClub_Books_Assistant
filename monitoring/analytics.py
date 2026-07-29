from collections import Counter
import json

from monitoring.database import get_connection

def get_total_queries():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT COUNT(*) FROM conversations"
    )
    total = cursor.fetchone()[0]
    conn.close()
    return total

def get_average_latency():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        """
        SELECT AVG(response_time)
        FROM conversations
        """
    )
    value = cursor.fetchone()[0]
    conn.close()
    return value or 0

def get_average_tokens():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        """
        SELECT AVG(total_tokens)
        FROM conversations
        """
    )
    value = cursor.fetchone()[0]
    conn.close()
    return value or 0

def get_recent_queries(limit=10):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        """
        SELECT
            question,
            response_time,
            total_tokens,
            created_at
        FROM conversations
        ORDER BY created_at DESC
        LIMIT ?
        """,
        (limit,),
    )
    rows = cursor.fetchall()
    conn.close()
    return rows

def get_feedback_stats():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        """
        SELECT
            COALESCE(feedback,'Not Rated'),
            COUNT(*)
        FROM conversations
        GROUP BY feedback
        """
    )
    rows = cursor.fetchall()
    conn.close()
    return rows

def get_latency_history():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        """
        SELECT response_time
        FROM conversations
        ORDER BY created_at
        """
    )
    rows = cursor.fetchall()
    conn.close()
    return [row[0] for row in rows]

def get_token_history():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        """
        SELECT total_tokens
        FROM conversations
        ORDER BY created_at
        """
    )
    rows = cursor.fetchall()
    conn.close()
    return [row[0] for row in rows]

def get_top_books():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        """
        SELECT sources
        FROM conversations
        """
    )
    rows = cursor.fetchall()
    conn.close()
    counter = Counter()
    for row in rows:
        if not row[0]:
            continue
        try:
            books = json.loads(row[0])
            if isinstance(books, list):
                counter.update(books)
        except Exception:
            books = [b.strip() for b in row[0].split(",")]
            counter.update(books)
    return counter.most_common(10)