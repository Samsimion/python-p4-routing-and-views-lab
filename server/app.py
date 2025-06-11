#!/usr/bin/env python3

from flask import Flask
app = Flask(__name__)


@app.route('/')
def index():
    return f'<h1>Python Operations with Flask Routing and Views</h1>'


@app.route('/print/<string:parameter>')
def print_parameter(parameter):
    print(parameter)
    return parameter

@app.route('/count/<int:count>')
def repeat(count):
    result = ""
    for i in range(count):
        result += f'{i}\n'
    return result

@app.route('/math/<int:num1>/<string:operation>/<int:num2>')
def math(num1, operation,num2):
    if operation == '+':
        result= num1+num2
    elif operation == '-':
        result= num1-num2
    elif operation == 'div':
        if num2 == 0:
            return "cant be devided by zero"
        result= num1/num2
    elif operation =='*':
        result= num1*num2
    elif operation == '%':
        result= num1%num2
    else:
        return f"mkuu wekaa mathematical operation"
    return f'{result}'
    

    
    



if __name__ == '__main__':
    app.run(port=5555,debug=True)

