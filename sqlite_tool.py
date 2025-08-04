from langchain.tools import tool
import sqlite3
import os

@tool
def get_sqlite(data: dict) -> str:
    """
    Executes a SQL query on a SQLite database file.

    Args:
        data (dict): A dictionary with 'db_path' and 'query' keys.

    Returns:
        str: Result of the SQL query or error message.
    """
    db_path = data.get("db_path")
    query = data.get("query")

    if not db_path or not query:
        return "❌ Missing 'db_path' or 'query'."

    if not os.path.exists(db_path):
        return f"❌ Database file not found: {db_path}"

    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute(query)
        rows = cursor.fetchall()
        conn.close()

        if not rows:
            return "✅ Query executed successfully. No rows returned."
        return f"✅ Query result:\n{rows}"

    except Exception as e:
        return f"❌ Error executing query: {str(e)}"
