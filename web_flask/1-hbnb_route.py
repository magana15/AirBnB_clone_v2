#!/usr/bin/python3
"""Starting web application with two routings
"""

from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello():
    """Return string when route is queried
    """
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    """Returns string when route queried
    """
    return 'HBNB'

if __name__ == '__main__':
    """set strict slashes then run"""
    app.url_map.strict_slashes = False
    app.run(host='0.0.0.0', port=5000)
