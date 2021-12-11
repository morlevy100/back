from flask import Flask, redirect, url_for
app = Flask(__name__)

@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'

@app.route('/home1')
def hello_home1():
    return redirect('/')

@app.route('/home2')
def hello_home2():
   return redirect(url_for('HELLO_WORLD'))

if __name__ == '__main__':
    app.run()
