# Put your app in here.
from flask import Flask, request
import operations

functions = {"add": operations.add,
             "sub": operations.sub,
             "mult": operations.mult,
             "div": operations.div}

app = Flask(__name__)


@app.get('/add')
def add():
    a = int(request.args['a'])
    b = int(request.args['b'])

    return str(operations.add(a, b))


@app.get('/sub')
def sub():
    a = int(request.args['a'])
    b = int(request.args['b'])

    return str(operations.sub(a, b))


@app.get('/mult')
def mult():
    a = int(request.args['a'])
    b = int(request.args['b'])

    return str(operations.mult(a, b))


@app.get('/div')
def div():
    a = int(request.args['a'])
    b = int(request.args['b'])

    return str(operations.div(a, b))


@app.get('/math/<function>')
def math(function):

    a = int(request.args['a'])
    b = int(request.args['b'])

    return str(functions[function](a, b))
