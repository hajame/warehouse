from flask import Flask, render_template
app = Flask(__name__)

class Product:
    def __init__(self, name, volume, amount):
        self.name = name
        self.volume = volume
        self.amount = amount

name = "Ontario"

info = ["Location: Canada", "Volume: 100000"]

products = []
products.append(Product("Bekant", 50, 2))
products.append(Product("Micke", 25, 10))
products.append(Product("Alex", 100, 2))
products.append(Product("Skarsta", 150, 5))
  
@app.route("/")
def hello():
    return render_template("index.html")

@app.route("/warehouse")
def content():
    return render_template("warehouse.html", name=name, info=info, products=products)

if __name__ == "__main__":
    app.run(debug=True)