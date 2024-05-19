#!/usr/bin/python3
"""Start an application with two routings
"""

from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello():
    """Returns a string when route is queried
    """
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    """Return string when route is queried
    """
    return 'HBNB'


@app.route('/c/<text>')
def c_is_fun(text):
    """Returns a reformated text
    """
    return 'C ' + text.replace('_', ' ')


@app.route('/python/')
@app.route('/python/<text>')
def python_with_text(text='is cool'):
    """format text based on optional variable
    """
    return 'Python ' + text.replace('_', ' ')


@app.route('/number/<int:n>')
def number(n=None):
    """Allow request if path variable is an integer
    """
    return str(n) + ' is a number'

if __name__ == '__main__':
    app.url_map.strict_slashes = False
    app.run(host='0.0.0.0', port=5000)
