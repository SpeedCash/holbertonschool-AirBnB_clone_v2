#!/usr/bin/python3
"""
Functions:
    app.route '/'
    app.route '/hbnb'
    app.route '/c/<text>'
    app.route '/python/<text>'
    app.route '/python'
Returns:
    text
"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Display 'Hello HBNB!'"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Display 'HBNB'"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """Display 'C + text replace'"""
    new_text = text.replace('_', ' ')
    return 'C ' + new_text


@app.route('/python', defaults={'text': 'is_cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text='is cool'):
    """Display 'Python + text repplace or Python + 'is cool'"""
    new_text = text.replace('_', ' ')
    return 'Python ' + new_text


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)