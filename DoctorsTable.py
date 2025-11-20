import sqlite3
conn = sqlite3.connect('Hospital.db')
cur =conn.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS doctors (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            type TEXT NOT NULL,
            phone TEXT
            )
            """)
conn.commit()
print('Table done')
conn.close()
