from flask import Flask, render_template, request
from helper import perform_calculation, convert_input
from rpn import evaluate_rpn

app = Flask(__name__)

history = []  # in-memory list; cleared on server restart


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/calculate', methods=['POST'])
def calculate():
    value1 = request.form['value1']
    value2 = request.form['value2']
    operation = str(request.form['operation'])
    numtype = request.form.get('numtype', 'float')

    if operation not in ['add', 'subtract', 'divide', 'multiply']:
        return render_template('index.html',
                               printed_result='Operation must be one of "add", "subtract", "divide", or "multiply".')

    try:
        value1, value2 = convert_input(value1, value2, numtype)
    except ValueError:
        return render_template('index.html',
                               printed_result='Invalid input — in integer mode, enter whole numbers only.')

    try:
        integer_mode = (numtype == 'int')
        result = perform_calculation(value1, value2, operation, integer_mode=integer_mode)
        result_str = str(round(result, 3))
        history.append(f"{value1} {operation} {value2} = {result_str}")
        return render_template('index.html', printed_result=result_str)
    except ZeroDivisionError:
        return render_template('index.html', printed_result='Cannot divide by zero')


@app.route('/history')
def show_history():
    return render_template('history.html', history=history)


@app.route('/rpn', methods=['GET', 'POST'])
def rpn():
    result = None
    error = None
    if request.method == 'POST':
        expression = request.form['expression']
        try:
            result = evaluate_rpn(expression)
            history.append(f"RPN: {expression} = {result}")
        except ValueError as e:
            error = str(e)
    return render_template('rpn.html', result=result, error=error)
