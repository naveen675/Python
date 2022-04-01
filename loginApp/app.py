from distutils.log import debug
from flask import Flask
from flask import request
import sqlite3

app = Flask(__name__)


def validateCredentials(username,password):

    userDbConnection = sqlite3.connect("user.db")
    print("Connected to USER Db")
    rows = (userDbConnection.execute(f'''
    SELECT Password FROM USERINFO WHERE UserID ="{username}"; '''))
    
    for row in rows:
        passwordInDb = row[0]
        if(str(passwordInDb) == password):
            return True
    return False

@app.route('/login/<username>,<password>', methods=["GET"])
def login(username,password):
    
    loginStatus = validateCredentials(username,password)
    if(loginStatus):
        return f"Login successful UserName: {username}"

    return "login Unsuccessful"

    


if __name__ == '__main__':
    app.run(debug=True)