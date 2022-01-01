from flask import Flask, redirect, url_for, request
from flask import render_template, session, Blueprint
import mysql.connector
from interact_with_DB import interact_db
from interact_with_DB import *

app = Flask(__name__)
app.secret_key = '12377'

assignment10 = Blueprint('assignment10', __name__,
                         static_folder='static',
                         static_url_path='/assignment10',
                         template_folder='templates')

insert_user = Blueprint('insert_user', __name__,
                        static_folder='static',
                        static_url_path='/insert_user',
                        template_folder='templates')

delete_user = Blueprint('delete_user', __name__,
                        static_folder='static',
                        static_url_path='/delete_user',
                        template_folder='templates')

update_user = Blueprint('update_user', __name__,
                        static_folder='static',
                        static_url_path='/update_user',
                        template_folder='templates')


@assignment10.route('/assignment10')
def index():
    query = 'select * from users;'
    users = interact_db(query=query, query_type='fetch')
    return render_template('assignment10.html', query=query, users=users)


@insert_user.route('/insert_user', methods=['POST'])
def index():
    name = request.form['name']
    email = request.form['email']
    id = request.form['id']
    password = request.form['password']
    query = "INSERT INTO users(name, email, id, password) VALUES ('%s', '%s', '%s', '%s');" % (name, email, id, password)
    interact_db(query=query, query_type='commit')
    return redirect('/assignment10')


@delete_user.route('/delete_user', methods=['POST'])
def index():
    id = request.form['id']
    query = "DELETE FROM users WHERE id='%s';" % id
    interact_db(query=query, query_type='commit')
    return redirect('/assignment10')

@update_user.route('/update_user', methods=['POST'])
def index():
    id = request.form['id']
    email = request.form['email']
    query = "UPDATE users SET email = '%s' WHERE id ='%s';" % (email, id)
    interact_db(query=query, query_type='commit')
    return redirect('/assignment10')