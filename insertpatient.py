import sqlite3
conn = sqlite3.connect('Hospital.db')
cur =conn.cursor()
name = input('Enter patient name: ')
condition = input('Enter condition: ')
phone = input('Enter patient number: ')
doctor = input('Enter Dr Id: ')
cur.execute(
    'INSERT INTO patients (name, condition, phone, doctor) VALUES (?,?,?,?)',
    (name,condition,phone,doctor)

    )
conn.commit()
print('patient inserted')
conn.close()