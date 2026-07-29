from monitoring.database import get_connection

def save_feedback(conversation_id: int, rating: str):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        """
        UPDATE conversations
        SET feedback=?
        WHERE id=?
        """,
        (rating, conversation_id,),
    )
    conn.commit()
    conn.close()

def get_feedback(conversation_id: int):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        '''
        SELECT feedback
        FROM conversations
        where id = ?
        ''',
        (conversation_id,),
    )
    row = cursor.fetchone()
    conn.close()
    if row:
        return row[0]
    return None