from flask import Flask, request
app = Flask(__name__)

@app.get('/welcome')
def say_welcome():
    return 'welcome'

@app.get('/welcome/home')
def say_welcome_home():
    return 'welcome home'

@app.get('/welcome/back')
def say_welcome_back():
    return 'welcome back'