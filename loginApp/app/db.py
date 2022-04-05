import sqlite3
conn = sqlite3.connect('users.db')
curr = conn.cursor()
query = """
    create table users(id int primary key, name varchar(100), user_id varchar(100), email varchar(80), password varchar(256));
"""
curr.execute(query)
conn.commit()
conn.close()