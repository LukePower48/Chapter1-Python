import sqlite3

# Connect to the existing hospital.db
conn = sqlite3.connect("hospital.db")
cur = conn.cursor()

# Create the doctors table
cur.execute("""
CREATE TABLE IF NOT EXISTS patients (
    id_ INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    condition TEXT NOT NULL,
    phone TEXT,
    doctor INTEGER
)
""")

conn.commit()
print("Table 'patients' created (if it didn't already exist).")

conn.close()
