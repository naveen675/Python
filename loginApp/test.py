import sqlite3
from flask import Flask

conn = sqlite3.connect("user.db")
print("Connected to Db")

create = conn.execute('''CREATE TABLE USERINFO 
        (Name STRING,
        UserID STRING,
        Password STRING);
''')
query = conn.execute("INSERT INTO USERINFO VALUES ('naveen','naveen675','122345')")
rows = conn.execute('''
    SELECT * FROM USERINFO ''')

con = conn.commit()

print(rows)
for row in rows:
    print("Name "+ row[0])
    print("User ID "+ row[1])
    print("Password "+ str(row[2]))


