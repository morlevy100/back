from flask import Flask, redirect, url_for
from flask import render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('cv.html')


@app.route('/assignment8')
def assignment8():
    return render_template('assignment8.html', hobbies=['pilates', 'surfing', 'reading'])


if __name__ == '__main__':
    app.run(debug=True)
