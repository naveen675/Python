import sqlite3
from flask import Flask


conn = sqlite3.connect("user.db")
print("Connected to Db")

# create = conn.execute('''CREATE TABLE USERINFO 
#         (Name STRING,
#         UserID STRING,
#         Password STRING);
# ''')

name = 'sai'
username = 'sai'
password = '123456'

query = f'''
  INSERT INTO USERINFO('Name','UserID','Password') VALUES ({name},{username},{password});'''
conn.execute(query)
rows = conn.execute('''
    SELECT * FROM USERINFO ''')

con = conn.commit()

print(rows)
for row in rows:
    print("Name "+ row[0])
    print("User ID "+ row[1])
    print("Password "+ str(row[2]))


# app = Flask(__name__)


# app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////tmp/test.db"
# db = SQLAlchemy(app)

# class Users(db.Model):

#    id = db.Column(db.Integer, primary_key=True)
#    name = db.Column(db.String(50))
#    username = db.column(db.String(60))
#    password = db.Column(db.String(50))


# db.create_all()

# if __name__ =="__main__":

#     app.run(debug=True)




