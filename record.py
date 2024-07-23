def search(column, text):
    import sqlite3
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute(f"SELECT login, balance FROM users WHERE {column} = ?", (text, ))
    searching = c.fetchall()
    if searching:
        username, balance = searching[0]
        return username, balance
    else:
        return None, None