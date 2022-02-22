from flask import Flask, render_template, request, url_for
from collections import OrderedDict

app = Flask(__name__)

cards = OrderedDict()
cards.update({
    '2': {'value': 0, 'count': 0},
    '3': {'value': 0, 'count': 0},
    '4': {'value': 0, 'count': 0},
    '5': {'value': 0, 'count': 0},
    '6': {'value': 0, 'count': 0},
    '7': {'value': 0, 'count': 0},
    '8': {'value': 0, 'count': 0},
    '9': {'value': 0, 'count': 0},
    '10': {'value': 0, 'count': 0},
    'J': {'value': 0, 'count': 0},
    'Q': {'value': 0, 'count': 0},
    'K': {'value': 0, 'count': 0},
    'A': {'value': 0, 'count': 0},
})

@app.route('/', methods=['GET'])
def index():
    submit_button = True
    return render_template('index.html', cards=cards, submit_button=submit_button)

@app.route('/operation_result/', methods=['POST'])
def operation_result():
    for card in cards:
        if not request.form[card]:
            cards[card]['count'] = 0
        else:
            cards[card]['count'] = int(request.form[card])
    cards['2']['value'] = cards['2']['count'] * 2
    cards['3']['value'] = cards['3']['count'] * 3
    cards['4']['value'] = cards['4']['count'] * 4
    cards['5']['value'] = cards['5']['count'] * 5
    cards['6']['value'] = cards['6']['count'] * 6
    cards['7']['value'] = cards['7']['count'] * 7
    cards['8']['value'] = cards['8']['count'] * 8
    cards['9']['value'] = cards['9']['count'] * 9
    cards['10']['value'] = cards['10']['count'] * 10
    cards['J']['value'] = cards['J']['count'] * (-2)
    cards['Q']['value'] = cards['Q']['count'] * (-4)
    cards['K']['value'] = cards['K']['count'] * (-6)
    cards['A']['value'] = cards['A']['count'] * (-8)

    values = [cards[x]['value'] for x in cards]
    result = sum(values)
    return render_template(
        "index.html",
        calculation_success=True,
        result=result,
    )
