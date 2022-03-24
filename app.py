from hashlib import new
from flask import Flask, render_template, redirect, session, flash
from flask_debugtoolbar import DebugToolbarExtension
from forms import Registration, Login
from models import connect_db, db, User

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///flask_feedback"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_ECHO"] = True
app.config["SECRET_KEY"] = "a secret key"

connect_db(app)
db.create_all()

toolbar = DebugToolbarExtension(app)


@app.route("/")
def homepage():
    """redirect to register for now"""
    if session["current_user"]:
        return render_template("secret.html")
    else:
        flash("you must login first", "danger")
        return redirect("/register")


@app.route("/register", methods=["GET", "POST"])
def register():
    """page to show registration form and register new users with information submitted from that form"""

    form = Registration()

    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        email = form.email.data
        first_name = form.first_name.data
        last_name = form.last_name.data

        new_user = User.register(username, password, email, first_name, last_name)
        db.session.add(new_user)
        db.session.commit()

        session["current_user"] = new_user.username

    else:
        return render_template("register.html", form=form)


@app.route("/login", methods=["GET", "POST"])
def login():
    """show login form and hangle login logic"""

    form = Login()

    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data

        user = User.authenticate(username, password)

        if user:
            session["current_user"] = user.username
            return redirect("/secret")
    else:
        return render_template("login.html", form=form)


@app.route("/secret")
def secret():
    """show just a secret page"""

    if session["current_user"]:
        return render_template("secret.html")
    else:
        flash("you must login first", "danger")
        return redirect("/")