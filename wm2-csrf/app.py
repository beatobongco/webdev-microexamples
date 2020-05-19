from flask import Flask, render_template, request
from forms import LoginForm

app = Flask(__name__)
app.config["SECRET_KEY"] = "you-will-never-guess"

TOTALLY_SECURE_PASSWORD = "ilikeeggs"


@app.route("/login", methods=["GET", "POST"])
def login():
    """A login route without CSRF protection.

    It just processes form data, allowing a login if the password supplied in the form matches
    the password defined in the TOTALLY_SECURE_PASSWORD variable
    """
    if request.method == "POST":
        if request.form["password"] == TOTALLY_SECURE_PASSWORD:
            return f"Logged in as user {request.form['username']}"
        else:
            return "Wrong password"
    return render_template("login.html", title="Sign In")


@app.route("/secure_login", methods=["GET", "POST"])
def secure_login():
    """A login route with CSRF protection.
    
    It will only allow requests that contain the correct CSRF token which is hidden in the login form.
    The result is that this endpoint should only accept requests from this particular form.

    You can see the CSRF token rendered in the form itself <input id="csrf_token" name="csrf_token" type="hidden" value="<token>">
    """
    form = LoginForm()
    if form.validate_on_submit():
        if form.password.data == TOTALLY_SECURE_PASSWORD:
            return f"Logged in as user {form.username.data}"
        else:
            return "Wrong password"
    return render_template("secure_login.html", title="Sign In", form=form)
