from flask import Flask, render_template, redirect, session, flash
from flask_debugtoolbar import DebugToolbarExtension
from forms import Registration
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

    return redirect("/register")

@app.route("/register", methods=["GET", "POST"])
def register():
    """page to show registration form and register new users with information submitted from that form"""

    form = Registration()

    if form.validate_on_submite():
        form
    else:
        return render_template("register.html", form=form)