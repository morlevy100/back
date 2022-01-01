
from flask import Flask, request
from flask import render_template, session, Blueprint
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
