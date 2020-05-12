"""Hello! Today we're going to learn about flask - a web microframework written in Python.

We're going to zoom into templates.

HTML file - a file that tells the browser what UI to show 
Templates - HTML files that allow you to plug in values to variables, conditionally show parts of the UI, loop through lists, etc

Templates are written in Jinja https://jinja.palletsprojects.com/en/2.11.x/

You can see the template file used in this example here: https://github.com/beatobongco/webdev-microexamples/blob/master/wm1-render_template/templates/base.html
"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
@app.route("/1")
def render_template_demo():
    # This is what the regular use of render_template looks like. You give it the name of your template and several variables to replace
    r = render_template(
        "base.html", title="This is my title", content="This is my content"
    )
    print("Type:", type(r))
    print("-" * 42)
    print("str representation", str(r))
    print("-" * 42)
    print("repr representation", repr(r))
    return r


def custom_render_template(template_name, *args, **kwargs):
    """Render an HTML template as a string
    
    replacing variables with the keys and values defined in keyword arguments 

    Variables:
        template_name - the name of your template file in your templates/ folder
        
    Genral python patterns:    
        *args - (list) all extra arguments without keywords will be placed here
        **kwargs - (dict) all extra keyword arguments will be placed here 
    """
    print("These are the kwargs", kwargs)

    # Open the file matching template_name inside the templates directory
    with open("templates/" + template_name, "r") as f:
        # Read all the contents of that file as a string
        template_string = f.read()
    # Iterate through the keys and values of the kwargs dict
    for k, v in kwargs.items():
        # Replace all instances of this pattern: {{s}} with the value of that key
        # NOTE: it will not work with spaces ex. {{ my_key }} , we can use regex to do that
        # but for the sake of simplicity we can illustrate this point with str.replace
        template_string = template_string.replace("{{" + k + "}}", v)
    # Return the transformed string
    return template_string


@app.route("/2")
def demo_page():
    r = custom_render_template(
        "base.html",
        title="Welcome!",
        content="These violent delights have violent ends",
    )
    print("Type:", type(r))
    print("-" * 42)
    print("str representation", str(r))
    print("-" * 42)
    print("repr representation", repr(r))
    return r


@app.route("/test")
def test_templating():
    r = render_template(
        "base.html", title="This is my title", content="This is my content"
    )
    r2 = custom_render_template(
        "base.html", title="This is my title", content="This is my content"
    )
    assert r == r2
    return "The two functions are equivalent"
