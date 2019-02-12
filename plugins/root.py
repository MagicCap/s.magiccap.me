from flask import redirect
# Imports redirect.

def root_route():
    return redirect("https://magiccap.me")
# The route for /.

def setup(app):
    app.add_url_rule("/", "root", root_route)
# Sets up the route.
