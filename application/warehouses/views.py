from application import app, db, login_required, login_manager
from flask import redirect, render_template, request, url_for
from flask_login import current_user

from application.warehouses.models import Warehouse, Warehouse_item
from application.warehouses.forms import WarehouseForm
from application.items.models import Item
from application.items.forms import ItemForm, AmountForm


@app.route("/warehouses/", methods=["GET"])
@login_required()
def warehouses_index():
    return render_template("warehouses/list.html", warehouses=current_user.warehouses)


@app.route("/warehouses/all", methods=["GET"])
@login_required(role="ADMIN")
def warehouses_all():
    return render_template("warehouses/list.html", warehouses=Warehouse.query.all())


@app.route("/warehouses/new/")
@login_required()
def warehouses_form():
    return render_template("warehouses/new.html", form=WarehouseForm(), warehouse_error="")


@app.route("/warehouses/<warehouse_id>/single/edit", methods=["GET", "POST"])
@login_required()
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
@login_required()
def warehouses_delete(warehouse_id):

    db.session.delete(Warehouse.query.get(warehouse_id))
    db.session().commit()

    return render_template("warehouses/list.html", warehouses=current_user.warehouses)


@app.route("/warehouses/<warehouse_id>/single", methods=["GET"])
@login_required()
def warehouse_single(warehouse_id):
    form = ItemForm(request.form)

    return render_template("warehouses/single.html", warehouse=Warehouse.query.get(warehouse_id), form=form)


@app.route("/warehouses", methods=["POST"])
@login_required()
def warehouses_create():
    form = WarehouseForm(request.form)

    if not form.validate():
        return render_template("warehouses/new.html", form=form, warehouse_error="")

    warehouse = Warehouse.query.filter_by(name=form.name.data).first()

    if warehouse:
        return render_template("warehouses/new.html", form=form, warehouse_error="Warehouse already exists")

    warehouse = Warehouse(form.name.data, form.volume.data)
    warehouse.users.append(current_user)

    db.session().add(warehouse)
    db.session().commit()

    return redirect(url_for("warehouses_index"))


@app.route("/warehouses/<warehouse_id>/single/<item_id>/", methods=["POST"])
@login_required()
def items_take_one(item_id, warehouse_id):

    t = Warehouse_item.query.filter_by(
        item_id=item_id, warehouse_id=warehouse_id).first()
    if t.amount > 0:
        t.amount = t.amount - 1
        db.session().commit()

    return redirect(url_for("warehouse_single", warehouse_id=warehouse_id))


@app.route("/warehouses/<warehouse_id>/single/<item_id>+/", methods=["POST"])
@login_required()
def items_add_one(item_id, warehouse_id):

    warehouse = Warehouse.query.get(warehouse_id)
    item = Item.query.get(item_id)
    warehouse_item = Warehouse_item.query.filter_by(item_id=item_id,
                                                    warehouse_id=warehouse_id).first()
    difference = item.volume
    
    if warehouse.fits(warehouse_id, difference):
        warehouse_item.amount = warehouse_item.amount + 1
        db.session().commit()

    return redirect(url_for("warehouse_single", warehouse_id=warehouse_id))


@app.route("/warehouses/<warehouse_id>/single/<item_id>/delete", methods=["GET"])
@login_required()
def warehouse_item_delete(item_id, warehouse_id):

    t = Warehouse_item.query.filter_by(
        item_id=item_id, warehouse_id=warehouse_id).first()
    db.session.delete(t)
    db.session().commit()

    return redirect(url_for("warehouse_single", warehouse_id=warehouse_id))


@app.route("/warehouses/<warehouse_id>/edit_amount/<item_id>", methods=["GET", "POST"])
@login_required()
def amount_edit(item_id, warehouse_id):

    if request.method == "GET":
        warehouse_item = Warehouse_item.query.filter_by(item_id=item_id,
                                                        warehouse_id=warehouse_id).first()
        item = Item.query.get(item_id)
        warehouse = Warehouse.query.get(warehouse_id)
        form = AmountForm(amount=warehouse_item.amount)
        return render_template("warehouses/edit_amount.html", item=item,
                               form=form, warehouse=warehouse, error="")

    warehouse = Warehouse.query.get(warehouse_id)
    item = Item.query.get(item_id)
    warehouse_item = Warehouse_item.query.filter_by(item_id=item_id,
                                                    warehouse_id=warehouse_id).first()
    form = AmountForm(request.form)

    if not form.validate():
        return render_template("warehouses/edit_amount.html", item=item,
                               form=form, warehouse=warehouse, error="")

    # Adds only if warehouse can fit the difference between the old and new amounts

    amount = form.amount.data
    difference = amount - warehouse_item.amount
    difference_volume = difference * item.volume

    if not warehouse.fits(warehouse_id, difference_volume):
        return render_template("warehouses/edit_amount.html", item=item,
                               form=form, warehouse=warehouse, error="Warehouse full")

    warehouse_item.amount = warehouse_item.amount + difference
    db.session().commit()

    return redirect(url_for("warehouse_single", warehouse_id=warehouse_id))
