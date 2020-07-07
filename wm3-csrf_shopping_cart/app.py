from flask import Flask, render_template, request, session, abort, redirect, url_for
from forms import LoginForm, BuyForm

app = Flask(__name__)
app.config["SECRET_KEY"] = "you-will-never-guess"

mock_db = {"paul": {"password": "fearisthemindkiller", "money": 1000, "items": []}}


@app.route("/clear")
def clear():
    # clears the session, effectively logging out our user for this toy app
    session.clear()
    return "OK"


@app.route("/login", methods=["GET", "POST"])
def secure_login():
    """A login route with CSRF protection.
    
    It will only allow requests that contain the correct CSRF token which is hidden in the login form.
    The result is that this endpoint should only accept requests from this particular form.

    You can see the CSRF token rendered in the form itself <input id="csrf_token" name="csrf_token" type="hidden" value="<token>">
    """
    form = LoginForm()
    if form.validate_on_submit():
        user = mock_db.get(form.username.data) or abort(401)
        if form.password.data == user["password"]:
            session["username"] = form.username.data
            return redirect(url_for("me"))
        else:
            return "Wrong password"
    return render_template("secure_login.html", title="Sign In", form=form)


@app.route("/")
def me():
    user = session.get("username")
    if not user:
        return redirect(url_for("secure_login"))
    return f"""<h1>Crysknives 'R Us</h1>
    <p>Logged in as user: {session['username']} | Money: {mock_db[user]['money']} <br> Items: {', '.join(mock_db[user]['items'])}</p>"""


@app.route("/buy", methods=["GET", "POST"])
def buy():
    form = BuyForm()
    if request.method == "GET":
        return render_template("buy.html", form=form)
    if form.validate_on_submit():
        return 1
