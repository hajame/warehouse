from application import app, db
from flask import redirect, render_template, request, url_for
from flask_login import login_required

from application.warehouses.models import Warehouse
from application.warehouses.forms import WarehouseForm


@app.route("/warehouses/", methods=["GET"])
@login_required
def warehouses_index():
    return render_template("warehouses/list.html", warehouses=Warehouse.query.all())


@app.route("/warehouses/new/")
@login_required
def warehouses_form():
    return render_template("warehouses/new.html", form=WarehouseForm())


@app.route("/warehouses/<warehouse_id>/single", methods=["GET"])
@login_required
def warehouse_single(warehouse_id):

    return render_template("warehouses/single.html", warehouse=Warehouse.query.get(warehouse_id))


@app.route("/warehouses", methods=["POST"])
@login_required
def warehouses_create():
    form = WarehouseForm(request.form)

    if not form.validate():
        return render_template("warehouses/new.html", form = form)

    warehouse = Warehouse(form.name.data, form.volume.data)
    db.session().add(warehouse)
    db.session().commit()

    return redirect(url_for("warehouses_index"))
