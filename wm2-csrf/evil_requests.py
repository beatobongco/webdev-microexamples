import requests

"""Imagine we are a malicious attacker"""

form_data = {"password": "ilikeeggs", "username": "john"}

# We want to login using the requests library and do some funky stuff
r = requests.post("http://localhost:5000/login", data=form_data)
# And we can! This assert shows that we are logged in
assert r.text == "Logged in as user john"

# If we want to try the same shenanigans on the seure_login page we cannot! Because we dont have the CSRF token
r = requests.post("http://localhost:5000/secure_login", data=form_data)

assert r.text != "Logged in as user john"
