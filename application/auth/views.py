from flask import render_template, request, redirect, url_for
from flask_login import login_user, logout_user, current_user

from application import app, db, login_required, login_manager
from application.auth.models import User, Role
from application.auth.forms import LoginForm, UserForm



@app.route("/auth/login", methods=["GET", "POST"])
def auth_login():
    if request.method == "GET":
        return render_template("auth/loginform.html", form=LoginForm())

    form = LoginForm(request.form)

    user = User.query.filter_by(
        username=form.username.data, password=form.password.data).first()
    if not user:
        return render_template("auth/loginform.html", form=form, error="No such username or password")

    login_user(user)
    return redirect(url_for("index"))

@app.route("/auth/list", methods=["GET"])
@login_required(role="ADMIN")
def users_all():
    return render_template("auth/list.html", users=User.query.all())


@app.route("/auth/new_user", methods=["GET", "POST"])
def auth_register():

    if request.method == "GET":
        return render_template("auth/new_user.html", form=UserForm())

    form = UserForm(request.form)

    if not form.validate():
        return render_template("auth/new_user.html", form = form)

    user = User(form.name.data, form.username.data, form.password.data)
    user.role = Role.query.get(1)
    
    db.session().add(user)
    db.session().commit()


    return redirect(url_for("auth_login"))

@app.route("/auth/edit_user/<user_id>", methods=["GET", "POST"])
@login_required(role="ADMIN")
def user_edit(user_id):

    if request.method == "GET":

        user = User.query.get(user_id)
        form = UserForm(name=user.name, username=user.username,
                        password=user.password, confirm=user.password)

        return render_template("auth/edit_user.html", form=form, user_id=user_id)

    form = UserForm(request.form)
    user = User.query.get(user_id)

    if not form.validate():
        return render_template("auth/edit_user.html", form=form, user_id=user_id)

    user.name = form.name.data
    user.username = form.username.data
    user.password = form.password.data
    

    db.session().commit()

    return redirect(url_for("users_all"))


@app.route("/auth/delete_user/<user_id>", methods=["GET"])
@login_required(role="ADMIN")
def user_delete(user_id):
    db.session.delete(User.query.get(user_id))
    db.session().commit()

    return render_template("auth/list.html", users=User.query.all())

@app.route("/auth/logout")
def auth_logout():
    logout_user()
    return redirect(url_for("index"))
