from application import app, db, login_required, login_manager
from flask import redirect, render_template, request, url_for
from flask_login import current_user

from application.items.models import Item
from application.warehouses.models import Warehouse, Warehouse_item
from application.items.forms import SearchForm, ItemEditForm, ItemForm, AmountForm

from sqlalchemy.sql import text


@app.route("/items/", methods=["GET"])
@login_required()
def items_index():
    return render_template("items/list.html", items=Item.query.all(), form=SearchForm(), warehouses=[])


@app.route("/items/new/")
@login_required()
def items_form():
    return render_template("items/new.html", form=ItemForm(), warehouse_error="")


@app.route("/items/", methods=["POST"])
@login_required()
def items_search():

    form = SearchForm(request.form)

    if not form.validate():
        return render_template("items/list.html", form=form)
    
    item = Item.query.filter_by(name=form.name.data).first()

    stmt = text("SELECT DISTINCT warehouse.id "
                "FROM warehouse, warehouse_item "
                "WHERE warehouse.id = warehouse_item.warehouse_id "
                "AND warehouse_item.item_id = :it ;").params(it=item.id)
    res = db.engine.execute(stmt)

    warehouses = []

    for row in res:
        a = Warehouse.query.get(row[0])
        warehouses.append(a)

    return render_template("items/list.html", items=Item.query.all(),
                    form=SearchForm(), warehouses=warehouses)


@app.route("/items/new", methods=["POST"])
@login_required()
def items_create():
    form = ItemForm(request.form)

    if not form.validate():
        return render_template("items/new.html", form=form, warehouse_error="")

    item = Item.query.filter_by(name=form.name.data).first()

    if not item:
        item = Item(form.name.data, form.volume.data)
        db.session().add(item)
        db.session().commit()

    warehouse = Warehouse.query.filter_by(name=form.warehouse.data).first()

    if not warehouse:
        return render_template("items/new.html", form=form, warehouse_error="No such warehouse.")

    comp = Warehouse_item.query.filter_by(item_id=item.id, warehouse_id=warehouse.id).first()

    if comp:
        if (comp.amount + form.amount.data) < 2147483648 and (comp.amount + form.amount.data) > -1:
            comp.amount = comp.amount + form.amount.data
            db.session().add(comp)
            db.session().commit()
    else:
        relation = Warehouse_item(warehouse, item, form.amount.data)
        db.session().add(relation)
        db.session().commit()

    return redirect(url_for("warehouse_single", warehouse_id=warehouse.id))


@app.route("/items/<item_id>/edit/", methods=["GET", "POST"])
@login_required()
def items_edit(item_id):

    if request.method == "GET":

        item = Item.query.get(item_id)
        form = ItemEditForm(obj=item)   

        return render_template("items/edit.html", form=form, item_id=item_id)

    form = ItemEditForm(request.form)
    item = Item.query.get(item_id) 
      
    if not form.validate():
        return render_template("items/edit.html", form=form, item_id=item_id)

    item.name = form.name.data
    item.volume = form.volume.data

    db.session().commit()

    return redirect(url_for("items_index"))

@app.route("/items/<item_id>/delete", methods=["GET"])
@login_required()
def items_delete(item_id):

    db.session.delete(Item.query.get(item_id))
    db.session().commit()

    return redirect(url_for("items_index"))