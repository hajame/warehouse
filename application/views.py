from flask import Flask, render_template
app = Flask(__name__)
from application import app

class Item:
    def __init__(self, name, volume, amount):
        self.name = name
        self.volume = volume
        self.amount = amount

name = "Ontario"

info = ["Location: Canada", "Volume: 100000"]

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/warehouse")
def content():
    return render_template("warehouse.html", name=name, info=info)

if __name__ == "__main__":
    app.run(debug=True)
