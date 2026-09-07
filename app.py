from flask import Flask
from poker.deck import Deck

app = Flask(__name__)

@app.route("/")
def home():
    return "Python Poker"
