def registration(ID):
    import sqlite3
    b = 10000
    conn = sqlite3.connect('../users.db')
    cur = conn.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS users
             (login TEXT, balance INTEGER)''')
    cur.execute("INSERT INTO users VALUES (?, ?)", (ID, b))
