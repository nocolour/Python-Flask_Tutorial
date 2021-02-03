# https://www.techwithtim.net/tutorials/flask/sessions/

from flask import Flask, redirect, url_for, render_template, request, session
from datetime import timedelta

app = Flask(__name__)
app.secret_key = "hello"
app.permanent_session_lifetime = timedelta(minutes=1)


@app.route("/")
def home():
    return render_template("index_sess.html")


@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        session.permanent = True
        user = request.form["nm"]
        session["user"] = user
        return redirect(url_for("user"))
    else:
        if "user" in session:
            return redirect(url_for("user"))

        return render_template("login_sess.html")


@app.route("/user")
def user():
    if "user" in session:
        user = session["user"]
        return f"<h1>You already login as {user}, will auto logout if idle after 1 minute!</h1>" + \
               f"<b><a href = '/logout'>click here to log out</a></b><br>" + \
               f"<b><a href = '/'>HOME</a></b>"

    else:
        return redirect(url_for("login"))


@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(debug=True)
