"""Hello! Today we're going to learn about flask - a web microframework written in Python.

We're going to zoom into templates.

HTML file - a file that tells the browser what UI to show 
Templates - HTML files that allow you to plug in values to variables, conditionally show parts of the UI, loop through lists, etc

Templates are written in Jinja https://jinja.palletsprojects.com/en/2.11.x/

You can see the template file used in this example here: https://github.com/beatobongco/webdev-microexamples/blob/master/wm1-render_template/templates/base.html
"""

from flask import Flask, render_template

app = Flask(__name__)

TITLE = "Welcome to Westworld"
CONTENT = "These violent delights have violent ends"
#
# Demo route 1 shows what render_template does
#
@app.route("/")
@app.route("/1")
def render_template_demo():
    # This is what the regular use of render_template looks like. You give it the name of your template and several variables to replace
    r = render_template("base.html", title=TITLE, content=CONTENT)
    print("Type:", type(r))
    print("-" * 42)
    print("str representation", str(r))
    print("-" * 42)
    print("repr representation", repr(r))
    return r


#
# Let's try to re-create what's happening inside the render_template function
#
def custom_render_template(template_name, *args, **kwargs):
    """Render an HTML template as a string
    
    replacing variables with the keys and values defined in keyword arguments 

    Variables:
        template_name - the name of your template file in your templates/ folder
        
    Genral python patterns:    
        *args - (list) all extra arguments without keywords will be placed here
        **kwargs - (dict) all extra keyword arguments will be placed here 
    """
    # Open the file matching template_name inside the templates directory
    # Read all the contents of that file as a string
    # Iterate through the keys and values of the kwargs dict
    # Replace all instances of this pattern: {{s}} with the value of that key
    # Return the transformed string

    # NOTE: this function will not work with spaces ex. {{ my_key }} , we can use regex to do that
    # but for the sake of simplicity we can illustrate this point with str.replace

    with open("templates/" + template_name, "r") as f:
        template_string = f.read()
    for k, v in kwargs.items():
        template_string = template_string.replace("{{" + k + "}}", v)
    return template_string


# The custom_render_template function is an oversimplification of what happens inside render_template
# but it illustrates that basically in the end it is parsing a string and doing string replacement
# ref: https://github.com/pallets/jinja/blob/3915eb5c2a7e2e4d49ebdf0ecb167ea9c21c60b2/src/jinja2/environment.py#L924

#
# Demo route 2 shows our custom template rendring function doing the exact same thing!
#
@app.route("/2")
def demo_page():
    r = custom_render_template("base.html", title=TITLE, content=CONTENT)
    print("Type:", type(r))
    print("-" * 42)
    print("str representation", str(r))
    print("-" * 42)
    print("repr representation", repr(r))
    return r


@app.route("/test")
def test_templating():
    """A route that tests if the outputs of both fucntions are the same"""
    r = render_template(
        "base.html", title="This is my title", content="This is my content"
    )
    r2 = custom_render_template(
        "base.html", title="This is my title", content="This is my content"
    )
    assert r == r2
    return "The two results are equivalent"


# A challenge: by modifying render_template and custom_render_template inputs and/or the base.html template,
# how can you force the /test route to fail?
