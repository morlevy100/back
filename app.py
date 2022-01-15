from flask import Flask, request, jsonify
from flask import render_template, session, Blueprint
import mysql.connector
import requests
import mysql.connector


from interact_with_DB import interact_db
from interact_with_DB import *

app = Flask(__name__)
app.secret_key = '12377'
app.config.from_pyfile('settings.py')

from pages.assignment10.assignment10 import assignment10

app.register_blueprint(assignment10)

from pages.assignment10.assignment10 import insert_user

app.register_blueprint(insert_user)

from pages.assignment10.assignment10 import delete_user

app.register_blueprint(delete_user)

from pages.assignment10.assignment10 import update_user

app.register_blueprint(update_user)


@app.route('/')
def index():
    return render_template('cv.html')


@app.route('/assignment8')
def assignment8():
    return render_template('assignment8.html', hobbies=['pilates', 'surfing', 'reading'])


users2 = ['tal', 'maya', 'chen', 'lee', 'ruth']


@app.route('/assignment9', methods=['GET', 'POST'])
def assignment9():
    flag = 'flag'
    output = ''
    if request.method == 'GET':
        if 'name' in request.args:
            session['name'] = request.args['name']
            if session['name'] == '':
                output = users2
            else:
                if session['name'] in users2:
                    output = 'your choice is:' + session['name']
                else:
                    output = 'user not found'
    else:
        if request.method == 'POST':
            if session['name']:
                session['name'] = ''
            else:
                session['name'] = request.form['name']
                flag = ''
    return render_template('assignment9.html', output=output, flag=flag)


@app.route('/assignment11/users', methods = ['POST', 'GET'])
def assignment11():
    i=0
    usersdic = {}
    query = 'select * from users;'
    users = interact_db(query=query, query_type='fetch')
    for user in users:
        usersdic = {
            f'id': users[i].id,
            'name': users[i].name,
            'email': users[i].email,
        }
        i = i+1
    return jsonify(usersdic)


def get_user(num):
    res = request.get(f'https://reqres.in/api/users?page=2')
    res = res.json()
    if num in res:
        return True
    else:
        return False


def get_users(num):
    res = requests.get(f'https://reqres.in/api/users/{num}')
    res = res.json()
    return res


@app.route('/assignment11/outer_source')
def req_backend_async_func():
    num = 2
    if "id" in request.args:
        num = int(request.args['id'])
    users = get_users(num)
    return render_template('assignment11.html', users=users)


@app.route('/assignment12/restapi_users/<int:USER_ID>')
def assignment12(USER_ID):
    query = 'select * from users where id=%s;' % USER_ID
    users = interact_db(query=query, query_type='fetch')
    if len(users) == 0:
        user_dict = {
            'status': 'failed',
            'message': 'user not found',
        }
    else:
        user_dict = {
            f'id': users[0].id,
            'name': users[0].name,
            'email': users[0].email,
        }
    return jsonify(user_dict)


@app.route('/assignment12/restapi_users/')
def assignment12null():
    query = 'select * from users where id=555;'
    users = interact_db(query=query, query_type='fetch')
    user_dict = {
        f'id': users[0].id,
        'name': users[0].name,
        'email': users[0].email,
    }
    return jsonify(user_dict)
