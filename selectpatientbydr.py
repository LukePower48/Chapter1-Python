import sqlite3

conn = sqlite3.connect("hospital.db")
cur = conn.cursor()

doctor = input('Enter doctor id: ')

cur.execute("SELECT name, phone FROM patients WHERE doctor = ?", (doctor,))
rows = cur.fetchall()

print(f"\nPatients with doctor '{doctor}':\n")
for name, phone in rows:
    print("Name:", name, "| Phone:", phone)

conn.close()