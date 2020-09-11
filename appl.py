"""
    Calculator
    ~~~~~~~~~~~~~~

    A Calculator made by Flask and jQuery.
"""
import re
from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

@app.route('/_calculate')

def calculate():
    req_num1 = request.args.get('number1', '0')
    operator = request.args.get('operator', '+')
    req_num2 = request.args.get('number2', '0')
    # validate the input data
    num1 = re.match(r'^\-?\d*[.]?\d*$', req_num1)
    num2 = re.match(r'^\-?\d*[.]?\d*$', req_num2)

    if num1 is None or num2 is None or operator not in '+-*/':
        return jsonify(result='Error!')

    if operator == '/':
        result = eval(req_num1 + operator + str(float(req_num2)))
    else:
        result = eval(req_num1 + operator + req_num2)
    return jsonify(result=result)


@app.route('/')

def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0')
