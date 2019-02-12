from flask import request, Blueprint, redirect
from tables import LinkShortener
import string
import random

short_blueprint = Blueprint("shorteners", __name__)

@short_blueprint.route("/<short>")
def shortened_link(short):
    try:
        short = LinkShortener.get(short)
    except LinkShortener.DoesNotExist:
        return "Link not found.", 404

    return redirect(short.url)

@short_blueprint.route("/add")
def add_link():
    url = request.args.get("url")
    if not url:
        return "URL not found.", 400

    chars = "".join([random.choice(string.ascii_letters + string.digits) for i in range(5)])

    LinkShortener(url=url, short=chars).save()

    return "https://s.magiccap.me/" + chars, 200

def setup(app):
    app.register_blueprint(short_blueprint)
