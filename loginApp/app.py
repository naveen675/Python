from flask import Flask, jsonify, make_response, request
from werkzeug.security import generate_password_hash,check_password_hash
from functools import wraps
import jwt
import datetime
import sqlite3

app = Flask(__name__)



app.config['SECRET_KEY'] = 'naveensainidamanuri'

# def token_required(f):
#     @wraps(f)
#     def decorator(*args,**kwargs):
        
#         print(token)
#         if not token:
#             return jsonify({'message':'Token is missing!'})
        
#         return f(*args, **kwargs)
#     return decorator 

# @app.route('/update')
# @token_required
# def update():
#     return jsonify({'message':'This is a valid token'})

@app.route('/login/<username>,<password>')
# @app.route('/login', methods=['GET']) 
def login(username,password):
 
    if password == '123456':

        token = jwt.encode({'user':username,'exp' : datetime.datetime.utcnow() + datetime.timedelta(minutes=45)},app.config['SECRET_KEY'])

        return jsonify({'token':token})
    
    return make_response('could not verify please do signup')


@app.route('/signup/<name>,<username>,<password>')
def signup(name,username,password):

    conn = sqlite3.connect("user.db")
    print("Connected to Db")

    try:
        query = f''' 
                INSERT INTO USERINFO VALUES ({name},{username},{password})
        '''
        conn.execute(query)
        conn.commit()
        return "query Excuted Success fully"

    except :
        return "Execution failed"






    

if __name__ == '__main__':
    app.run(debug = True)