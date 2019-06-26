import json
from datetime import datetime
from time import sleep

from flask import Flask, flash, jsonify, redirect, render_template, request
from flask_bootstrap import Bootstrap

# This is a Flask thing and needs to stay, don't know why it is in
# a separate function.
def create_app():
    app = Flask(__name__)
    Bootstrap(app)

    return app

app = create_app()


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/whoswho')
def whoswho():
    return render_template('whoswho.html')


@app.route('/colour', methods=['GET'])
def house_colour():
    '''Returns an who has a (colour) house.'''
    value = request.args['value']

    if value == 'yellow':
        return_string = 'Norwegian'
    elif value == 'blue':
        return_string = 'Ukranian'
    elif value == 'red':
        return_string = 'Englishman'
    elif value == 'ivory':
        return_string = 'Spaniard'
    elif value == 'green':
        return_string = 'Japanese'
    else:
        return_string = 'No idea!'

    return json.dumps(return_string)

@app.route('/nationality', methods=['GET'])
def drink_type():
    '''Returns a what is drunk by the (nationality) person.'''
    value = request.args['value']

    if value == 'norwegian':
        return_string = 'water'
    elif value == 'ukrainian':
        return_string = 'tea'
    elif value == 'englishman':
        return_string = 'milk'
    elif value == 'spaniard':
        return_string = 'orange juice'
    elif value == 'japanese':
        return_string = 'coffee'
    else:
        return_string = 'No idea!'

    return json.dumps(return_string)

@app.route('/pet', methods=['GET'])
def pet():
    '''Returns an who has a (creature) pet.'''
    value = request.args['value']

    if value == 'fox':
        return_string = 'Norwegian'
    elif value == 'horse':
        return_string = 'Ukranian'
    elif value == 'snails':
        return_string = 'Englishman'
    elif value == 'dog':
        return_string = 'Spaniard'
    elif value == 'zebra':
        return_string = 'Japanese'
    else:
        return_string = 'No idea!'

    return json.dumps(return_string)

@app.route('/smokes', methods=['GET'])
def smokes():
    '''Returns an who smokes (smokes).'''
    value = request.args['value']

    if value == 'kools':
        return_string = 'Norwegian'
    elif value == 'chesterfields':
        return_string = 'Ukranian'
    elif value == 'old-golds':
        return_string = 'Englishman'
    elif value == 'lucky-strikes':
        return_string = 'Spaniard'
    elif value == 'parliaments':
        return_string = 'Japanese'
    else:
        return_string = 'No idea!'

    return json.dumps(return_string)


if __name__ == '__main__':
    app.run(debug=True)
