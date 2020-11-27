import mysql.connector

conn = mysql.connector.connect(
    host = 'localhost',
    username = 'root',
    password = '',
    database = 'first'
)

cursor = conn.cursor()

selectq = "select * from first1"

cursor.execute(selectq)
record = cursor.fetchall()

print("Names", cursor.rowcount)

for i in record:
    print("id",i[0])

