import json

from monitoring.database import get_connection
from monitoring.schema import ConversationLog

def save_conversation(log: ConversationLog) -> int:
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        """
        INSERT INTO conversations(
            question,
            answer,
            model,
            retriever,
            sources,
            prompt_tokens,
            completion_tokens,
            total_tokens,
            response_time,
            feedback
        )
        VALUES(?,?,?,?,?,?,?,?,?,?)
        """,
        (
            log.question,
            log.answer,
            log.model,
            log.retriever,
            json.dumps(log.sources),
            log.prompt_tokens,
            log.completion_tokens,
            log.total_tokens,
            log.response_time,
            log.feedback,
        ),
    )
    conn.commit()
    conversation_id = cursor.lastrowid
    conn.close()
    return conversation_id