from ast import Global
from flask import Flask,jsonify,request
import jwt
import datetime
from functools import wraps

app = Flask(__name__)

token = None

app.config['SECRET_KEY'] = 'naveensainidamanuri'

def token_required(f):
    @wraps(f)
    def decorator(*args,**kwargs):
        
        print(token)
        if not token:
            return jsonify({'message':'Token is missing!'})
        
        return f(*args, **kwargs)
    return decorator 

@app.route('/update')
@token_required
def update():
    return jsonify({'message':'This is a valid token'})

@app.route('/login/<username>,<password>')
def login(username,password):

    if (password == '123456'):

        token = jwt.encode({'user':username,'exp':datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, app.config['SECRET_KEY'])
        return token
    else:
        return "invalid"

if __name__ == '__main__':
    app.run(debug = True)