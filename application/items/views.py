from application import app, db
from flask import redirect, render_template, request, url_for
from application.items.models import Item

@app.route("/items/", methods=["GET"])
def items_index():
    return render_template("items/list.html", items = Item.query.all())

@app.route("/items/new/")
def items_form():
    return render_template("items/new.html")

@app.route("/items/<item_id>/", methods=["POST"])
def items_take_one(item_id):

    t = Item.query.get(item_id)
    if t.amount > 0:
        t.amount = t.amount - 1
    db.session().commit()
  
    return redirect(url_for("items_index"))

@app.route("/items/<item_id>+/", methods=["POST"])
def items_add_one(item_id):

    t = Item.query.get(item_id)
    t.amount = t.amount + 1
    db.session().commit()
  
    return redirect(url_for("items_index"))

@app.route("/items", methods=["POST"])
def items_create():
    item = Item(request.form.get("name"), request.form.get("volume"), request.form.get("amount"))
    db.session().add(item)
    db.session().commit()

    return redirect(url_for("items_index"))