import sqlite3
conn = sqlite3.connect('Hospital.db')
cur =conn.cursor()
name = input('Enter Dr name: ')
typ = input('Enter Dr type: ')
phone = input('Enter Dr number: ')
cur.execute(
    'INSERT INTO doctors (name, type, phone) VALUES (?,?,?)',
    (name,typ,phone)

    )
conn.commit()
print('Dr inserted')
conn.close()