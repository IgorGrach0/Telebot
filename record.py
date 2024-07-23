def search(column, text):
    import sqlite3
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute(f"SELECT * FROM users WHERE {column} = ?", (text, ))
    searching = c.fetchall()
    if searching:
        return True
    else:
        return False