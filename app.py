from flask import Flask, render_template
from poker.deck import Deck

app = Flask(__name__)

@app.route("/")
def home():
    deck = Deck()
    return render_template("index.html", deck=deck)

