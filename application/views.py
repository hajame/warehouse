from flask import Flask, render_template
app = Flask(__name__)
from application import app
from application.warehouses.models import Warehouse
from application.items.models import Item

@app.route("/")
def index():
    return render_template("index.html", warehouse_count=Warehouse.count_warehouses(), item_count=Item.count_items())

@app.route("/warehouse")
def content():
    return render_template("warehouse.html", name=name, info=info)

if __name__ == "__main__":
    app.run(debug=True)
    