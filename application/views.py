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

items = []
items.append(Item("Bekant", 50, 3))
items.append(Item("Micke", 25, 10))
items.append(Item("Alex", 100, 2))
items.append(Item("Skarsta", 150, 5))
  
@app.route("/")
def hello():
    return render_template("index.html")

@app.route("/warehouse")
def content():
    return render_template("warehouse.html", name=name, info=info, items=items)

if __name__ == "__main__":
    app.run(debug=True)
