import requests

"""Imagine we are a malicious attacker"""

form_data = {"password": "ilikeeggs", "username": "john"}

# We want to login using the requests library and do some funky stuff
r = requests.post("http://localhost:5000/login", data=form_data)
# And we can! This assert shows that we are logged in
assert r.text == "Logged in as user john"

# If we want to try the same shenanigans on the secure_login page...
r = requests.post("http://localhost:5000/secure_login", data=form_data)
# We cannot! Because we dont have the CSRF token
assert r.text != "Logged in as user john"

# Beware, if somehow the attacker gets your CSRF token, they could simply change the request to
# include the token and be able to successfully execute requests

# It would simply look something like this
form_data = {"password": "ilikeeggs", "username": "john", "csrf_token": "<token>"}
r = requests.post("http://localhost:5000/secure_login", data=form_data)

# Thankfully this is difficult to do because the CSRF are generated cryptographically using
# a combination of a secret string and a timestramp, and are only valid for a while
# https://portswigger.net/web-security/csrf/tokens
