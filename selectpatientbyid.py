import sqlite3

conn = sqlite3.connect("hospital.db")
cur = conn.cursor()

id_ = input('Enter patient id: ')

cur.execute("SELECT name, phone FROM patients WHERE id_ = ?", (id_,))
rows = cur.fetchall()

print(f"\nPatients with id '{id_}':\n")
for name, phone in rows:
    print("Name:", name, "| Phone:", phone)

conn.close()