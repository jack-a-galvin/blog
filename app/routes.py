from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
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