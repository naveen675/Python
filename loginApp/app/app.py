import sqlite3
from flask import Flask, request, jsonify, make_response
from werkzeug.security import generate_password_hash, check_password_hash
import jwt
import datetime
from functools import wraps
import uuid

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'

def connect():
    conn = sqlite3.connect('users.db')
    conn.row_factory = sqlite3.Row
    return conn


def token_required(f):
    @wraps(f)
    def decorator(*args, **kwargs):
        token = None
        if 'x-access-tokens' in request.headers:
            token = request.headers['x-access-tokens']

        if not token:
            return make_response({'message': 'a valid token is missing'})
        try:
            data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])
            user_id = data['user_id']
            conn = connect()
            cursor = conn.cursor()
            cursor.execute(f"select * from users where user_id='{user_id}'")
            user = cursor.fetchall()[0]
            conn.close()
            return f(user, *args, **kwargs)
        except:
            return jsonify({'message': 'token is invalid'})
    return decorator


@app.route('/signup', methods=['POST'])
def signup():
    data = request.json
    con = connect()
    email = data['email']
    name = data['name']
    password = data['password']
    cursor = con.cursor()
    cursor.execute(f"select email from users where email='{email}';")
    data = cursor.fetchall()
    if data:
        return make_response('failed', 409, {'msg': 'user already exists'})
    else:
        hashed_password = generate_password_hash(password)
        query = "insert into users(name, user_id, email, password) values('{0}', '{1}', '{2}', '{3}')".format(name, str(uuid.uuid4()), email, hashed_password)
        cursor.execute(query)
        con.commit()
        con.close()
    return make_response('success', 200, {'message': 'user crated successully'})

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    email = data['email']
    password = data['password']
    conn = connect()
    cursor = conn.cursor()
    cursor.execute(f"select * from users where email='{email}'")
    data = cursor.fetchall()
    if data:
        data = data[0]
        if check_password_hash(data['password'], password):
            token = jwt.encode({'user_id' : data['user_id'], 'exp' : datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, app.config['SECRET_KEY'], "HS256")
            return make_response({'token': token, "message": "login successful"}, 200)
        else:
            return make_response('failed', 400, {'msg': 'password miss match'})
    return make_response('failed', 400, {'msg': 'user doesnot exist'})

@app.route('/update', methods=['PUT'])
@token_required
def update(user):
    data = request.json
    user_id = user['user_id']
    con = connect()
    cursor = con.cursor()
    for field, value in data.items():
        if field is not None:
            if field == 'password':
                value = generate_password_hash(value)
            cursor.execute(f"update users set {field} = '{value}' where user_id='{user_id}';")
            con.commit()
    con.close()
    return make_response({"message": "successfully updated user details"}, 200)


@app.route('/delete', methods=['DELETE'])
@token_required
def delete(user):
    con = connect()
    cursor = con.cursor()
    user_id = user['user_id']
    cursor.execute(f"delete from users where user_id='{user_id}';")
    con.commit()
    con.close()
    return make_response({"message": "successfully deleted user"}, 200)




if __name__ == '__main__':
    app.run(debug=True)

