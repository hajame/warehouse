from application import app, db
from flask import redirect, render_template, request, url_for
from flask_login import login_required, current_user

from application.warehouses.models import Warehouse, Warehouse_item
from application.warehouses.forms import WarehouseForm
from application.items.models import Item
from application.items.forms import ItemForm


@app.route("/warehouses/", methods=["GET"])
@login_required
def warehouses_index():
    return render_template("warehouses/list.html", warehouses=Warehouse.query.all())


@app.route("/warehouses/new/")
@login_required
def warehouses_form():
    return render_template("warehouses/new.html", form=WarehouseForm())


@app.route("/warehouses/<warehouse_id>/single/edit", methods=["GET", "POST"])
@login_required
def warehouses_edit(warehouse_id):

    if request.method == "GET":

        wh = Warehouse.query.get(warehouse_id)
        form = WarehouseForm(obj=wh)

        return render_template("warehouses/edit.html", form=form, warehouse_id=warehouse_id)

    form = WarehouseForm(request.form)
    wh = Warehouse.query.get(warehouse_id)

    if not form.validate():
        return render_template("warehouses/edit.html", warehouse_id=warehouse_id, form=form)

    wh.name = form.name.data
    wh.volume = form.volume.data

    db.session().commit()

    return redirect(url_for("warehouse_single", warehouse_id=warehouse_id))


@app.route("/warehouses/<warehouse_id>/single/delete", methods=["GET"])
@login_required
def warehouses_delete(warehouse_id):

    db.session.delete(Warehouse.query.get(warehouse_id))
    db.session().commit()

    return render_template("warehouses/list.html", warehouses=Warehouse.query.all())


@app.route("/warehouses/<warehouse_id>/single", methods=["GET"])
@login_required
def warehouse_single(warehouse_id):
    form = ItemForm(request.form)

    return render_template("warehouses/single.html", warehouse=Warehouse.query.get(warehouse_id), form = form)


@app.route("/warehouses", methods=["POST"])
@login_required
def warehouses_create():
    form = WarehouseForm(request.form)

    if not form.validate():
        return render_template("warehouses/new.html", form=form)

    warehouse = Warehouse(form.name.data, form.volume.data)
    warehouse.users.append(current_user)

    db.session().add(warehouse)
    db.session().commit()

    return redirect(url_for("warehouses_index"))

@app.route("/warehouses/<warehouse_id>/single/<item_id>/", methods=["POST"])
@login_required
def items_take_one(item_id, warehouse_id):

    t = Warehouse_item.query.filter_by(item_id=item_id, warehouse_id=warehouse_id).first()
    if t.amount > 0:
        t.amount = t.amount - 1
    db.session().commit()

    return redirect(url_for("warehouse_single", warehouse_id = warehouse_id))


@app.route("/warehouses/<warehouse_id>/single/<item_id>+/", methods=["POST"])
@login_required
def items_add_one(item_id, warehouse_id):

    t = Warehouse_item.query.filter_by(item_id=item_id, warehouse_id=warehouse_id).first()
    if t.amount < 2147483647:
        t.amount = t.amount + 1
    db.session().commit()

    return redirect(url_for("warehouse_single", warehouse_id = warehouse_id))


@app.route("/warehouses/<warehouse_id>/single/<item_id>/delete", methods=["GET"])
@login_required
def warehouse_item_delete(item_id, warehouse_id):

    t = Warehouse_item.query.filter_by(item_id=item_id, warehouse_id=warehouse_id).first()
    db.session.delete(t)
    db.session().commit()

    return redirect(url_for("warehouse_single", warehouse_id = warehouse_id))