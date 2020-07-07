from flask import render_template, flash, redirect, url_for, request, session
from flask_login import login_user, logout_user, current_user, login_required, COOKIE_NAME
from flask_login.utils import decode_cookie, _cookie_digest
from werkzeug.urls import url_parse
from app import app, db
from app.forms import LoginForm, RegistrationForm
from app.models import User


@app.route('/')
@app.route('/index')
@login_required
def index():
    # When you tick "Remember me", it leaves a cookie in your browser
    # <show chrome devtools>
    # The cookie is named `remember_token`
    print("Remember me cookie name:", COOKIE_NAME)
    # >> Remember me cookie name: remember_token
    
    # You can access cookies through chrome or through flask.request.cookies
    cookie = request.cookies.get(COOKIE_NAME)
    # You'll see a value delimited by a pipe |
    # It represents user_id|digest
    print(COOKIE_NAME,":", cookie)
    # >> remember_token : 1|317ae4390a37e7ac78bd4bfb083e6482e068cc9d9a1077ed23df1c3df92fbf1d0503ee435ab52fba09d4a4f53c469b9b938104ff5010bdf56d30b4e56dfd8c42 
    
    # digest in the cookie should match an internal function that returns a string based on the user_id
    user_id, digest = cookie.rsplit(u'|', 1)
    print("Cookie digest:", digest) 
    internal_digest = _cookie_digest(user_id)
    print("Internally generated digest:", internal_digest)
    # >> Cookie digest: 317ae4390a37e7ac78bd4bfb083e6482e068cc9d9a1077ed23df1c3df92fbf1d0503ee435ab52fba09d4a4f53c469b9b938104ff5010bdf56d30b4e56dfd8c42
    # >> Internally generated digest: 317ae4390a37e7ac78bd4bfb083e6482e068cc9d9a1077ed23df1c3df92fbf1d0503ee435ab52fba09d4a4f53c469b9b938104ff5010bdf56d30b4e56dfd8c42
    
    print("Do they match?", digest == internal_digest)
    # >> Do they match? True 
    
    # if they match, return the user_id (called the payload)
    print("decoded cookie:", decode_cookie(cookie))
    # >> decoded cookie: 1

    # Let's try "faking a cookie"
    fake_cookie = "1|I'mTryingToGuessTheDigest"
    print("Trying to decode a fake cookie results in:", decode_cookie(fake_cookie))
    # >> Trying to decode a fake cookie results in: None
    
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', title='Home', posts=posts)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)
