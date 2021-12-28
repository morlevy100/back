from flask import Flask, redirect, url_for, request
from flask import render_template, session

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('cv.html')


@app.route('/assignment8')
def assignment8():
    return render_template('assignment8.html', hobbies=['pilates', 'surfing', 'reading'])


users = ['tal', 'maya', 'chen', 'lee', 'ruth']
app.secret_key = '222'


@app.route('/assignment9', methods=['GET', 'POST'])
def assignment9():
    flag = 'flag'
    output = ''
    if request.method == 'GET':
        if 'name' in request.args:
            session['name'] = request.args['name']
            if session['name'] == '':
                output = users
            else:
                if session['name'] in users:
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
    return render_template('assignment9.html', output = output, flag = flag)



if __name__ == '__main__':
    app.run(debug=True)

users = ['tal', 'maya', 'chen', 'lee', 'ruth']
