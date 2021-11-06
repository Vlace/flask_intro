# Put your app in here.
from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)

@app.route('/')
def home():
    return 'welcome'

@app.route('/<oper>')
def operations(oper):
    operation = {
    "add": add,
    "sub": sub,
    "mult": mult,
    "div": div,
        }
    a = request.args.get('a')
    b = request.args.get('b')
    final = operation[oper](int(a),int(b))

    return str(final)

@app.route('/math/<oper>')
def math_ops(oper):
    operation = {
    "add": add,
    "sub": sub,
    "mult": mult,
    "div": div,
        }
    a = request.args.get('a')
    b = request.args.get('b')
    final = operation[oper](int(a),int(b))

    return str(final)
