from flask import Flask, render_template, request, url_for
from collections import OrderedDict

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    submit_button = True
    return render_template('index.html', submit_button=submit_button)

@app.route('/operation_result1', methods=['POST'])
def operation_result1():
    # to get result from post, use request.form('id')
    hearts = int(request.form['q1_hearts'])
    diamonds = int(request.form['q2_diamonds'])

    result = hearts*2 + diamonds*2
    return render_template(
        "index.html",
        calculation_success=True,
        result=result,
    )

@app.route('/operation_result1', methods=['POST'])
def operation_result2():
    spades = request.form['q1_spades']
    clubs = request.form['q2_clubs']


    result = spades*10 + clubs*10
    return render_template(
        "index.html",
        calculation_success=True,
        result=result,
    )