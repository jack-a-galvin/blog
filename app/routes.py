from flask import render_template, flash, redirect, url_for
from flask_login import current_user, login_user
from app import app
from app.forms import LoginForm
from app.models import User

@app.route("/")
@app.route("/index")
def index():
    user = {"username": "Jack"},
    posts = [
        {
            "author": {"username": "Johnny"},
            "body": "Quarantine is sooo BORING"
        },
        {
            "author": {"username": "Alex"},
            "body": "Please wear a mask guys"
        }
    ]
    return render_template("index.html", title="Little Blog", user=user, posts=posts)


@app.route("/login", methods=["GET","POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash("User:{} has requested to login. Remember Me:{}".format(form.username.data, form.remember_me.data))
        return redirect(url_for("index"))
    return render_template("login.html", title="Sign In", form=form)