# Put your app in here.
from flask import Flask, request

app = Flask(__name__)

@app.get('/add')
def add():
    """Adds two parameter inputs"""
    a = int(request.args["a"])
    b = int(request.args["b"])

    return str(a + b)

@app.get('/sub')
def sub():
    """Subtracts two parameter inputs"""
    a = int(request.args["a"])
    b = int(request.args["b"])

    return str(a - b)

@app.get('/mult')
def mult():
    """Multiplies two parameter inputs"""
    a = int(request.args["a"])
    b = int(request.args["b"])

    return str(a * b)

@app.get('/div')
def div():
    """Divides two parameter inputs"""
    a = int(request.args["a"])
    b = int(request.args["b"])

    return str(a / b)