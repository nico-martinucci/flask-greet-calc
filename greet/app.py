from flask import Flask

app = Flask(__name__)

@app.get('/welcome')
def say_welcome():
    """Return simple "welcome" Greeting."""

    return 'welcome'

@app.get('/welcome/home')
def say_welcome_home():
    """Return simple "welcome home" Greeting."""

    return 'welcome home'

@app.get('/welcome/back')
def say_welcome_back():
    """Return simple "welcome back" Greeting."""

    return 'welcome back'