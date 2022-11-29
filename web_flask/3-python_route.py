#!/usr/bin/python3
''' *** *** '''


from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    ''' *** *** '''
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    ''' *** *** '''
    return 'HBNB'


@app.route('/c/<text>')
def c_is(text):
    ''' *** *** '''
    return f'C {text}'.replace('_', " ")

@app.route('/python', strict_slashes=False)
@app.route('/python/<text>')
def python(text='is cool'):
    ''' *** *** '''
    return f'Python {text}'.replace('_', " ")

if __name__ == "__main__":
    """ Main Function """
    app.run(host='0.0.0.0', port=5000)
