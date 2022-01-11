from flask import Flask, request
from flask import render_template, session, Blueprint
import mysql.connector
import requests
import aiohttp
import random
import asyncio
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


@app.route('/assignment11/users')
def assignment11():
    db = mysql.connector.connect(host='127.0.0.1',
                                 user='root',
                                 passwd='root',
                                 db='users',s
                                 port=3306)
    cursor = db.cursor(dictionary=True)
    cursor.execute("select * from users;")
    result = cursor.fetchall()
    return render_template(result=result)


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



