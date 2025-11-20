import sqlite3
conn = sqlite3.connect('Hospital.db')
print ('Database Created')
conn.close()
