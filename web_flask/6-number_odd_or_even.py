#!/usr/bin/python3
"""
Functions:
    app.route '/'
    app.route '/hbnb'
    app.route '/c/<text>'
    app.route '/python/<text>'
    app.route '/python'
    app.route '/number/<int:n>'
    app.route '/number_template/<int:n>'
    app.route '/number_odd_or_even/<n>'
Returns:
    text
"""

from flask import Flask, render_template

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


@app.route('/number/<int:n>', strict_slashes=False)
def n_is_integer(n):
    """Display 'n is a number'"""
    return '{} is a number'.format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def n_template(n):
    """Display render_template"""
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def n_odd_or_even(n):
    """Display render_template even|odd"""
    if n % 2 == 0:
        return render_template('6-number_odd_or_even.html', n=n, text='even')
    else:
        return render_template('6-number_odd_or_even.html', n=n, text='odd')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)