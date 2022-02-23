from flask import Flask, render_template, request, url_for
from collections import OrderedDict

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    submit_button = True
    return render_template('index.html', submit_button=submit_button)

def get_form(id):
    r = request.form[id]
    if not r:
        return 0
    else:
        return int(r)

@app.route('/operation_result1', methods=['POST'])
def operation_result1():
    heart = get_form('f1_heart')
    heart_total = get_form('f1_heart_total')
    diamond = get_form('f1_diamond')
    club = get_form('f1_club')
    spade = get_form('f1_spade')
    king = get_form('f1_king')
    queen = get_form('f1_queen')
    jack = get_form('f1_jack')
    ace = get_form('f1_ace')
    two = get_form('f1_two')
    three = get_form('f1_three')

    if diamond < 3:
        X = 4
    else:
        X = 12

    if spade < 3:
        Y = 1
    else:
        Y = 0

    Z = min(heart, diamond, club, spade)

    if heart_total == 1:
        U = 6
    else:
        U = 2

    result = X*min(spade, heart) + diamond + U*heart + 6*Y*(spade + int(diamond/2)) + 2*(king + queen + jack) - 2*(ace + two + three) + 6*Z
    return render_template(
        "index.html",
        calculation_success=True,
        result=result
    )

@app.route('/operation_result2', methods=['POST'])
def operation_result2():
    # If you have more than 7 red cards, remove all black cards
    # If you have less than 4 red cards, remove all red cards
    heart = get_form('f2_heart')
    heart_ace = get_form('f2_heart_ace')
    diamond = get_form('f2_diamond')
    club = get_form('f2_club')
    spade = get_form('f2_spade')
    seven = get_form('f2_seven')
    ten = get_form('f2_ten')
    straight = get_form('f2_straight')
    underfive = get_form('f2_underfive')
    V = get_form('f2_triples')

    Z = min(heart, diamond, club, spade)

    if not heart:
        X = 2
    else:
        X = 1

    if not spade:
        Y = 0.5
    else:
        Y = 1

    if not spade and not club:
        U = 10
    else:
        U = 0

    result = spade + X*diamond + heart + 2*Z + 4*heart_ace + 2*Y*spade + 2*seven - 2*ten + U + 7*V

    if straight:
        result*=2

    if underfive:
        result*=3


    return render_template(
        "index.html",
        calculation_success=True,
        result=result,
    )