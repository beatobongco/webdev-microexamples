## CSRF Demo 

A very simple demo showing how flask-wtf helps us deal with CSRF attacks. 

### What is CSRF?

Cross-site request forgery, can be pronounced as "sea surf" or you could just say C-S-R-F but that's not too cool jk

In a CSRF attack, an innocent end user is tricked by an attacker into submitting a web request that they did not intend. This may cause actions to be performed on the website that can include inadvertent client or server data leakage, change of session state, or manipulation of an end user's account. 

[src](https://en.wikipedia.org/wiki/Cross-site_request_forgery)

### How to use this demo

1. Install the requirements
2. Run `./run.sh` to run the flask app

Look inside `evil_requests.py`

TODO: Explain how this attack can affect you if you are logged into a shopping website and an attacker exploits a form to force you to buy stuff

### Extra resouces

How CSRF tokens are validated in flask-wtf: https://github.com/lepture/flask-wtf/blob/master/flask_wtf/csrf.py#L59
