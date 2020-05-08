from flask import Blueprint
import os
from .tasks import make_file

bp = Blueprint("all", __name__)

@bp.route("/")
def index():
    return "Hello"

@bp.route("/<string:fname>/<string:contents>")
def makefile(fname, content):
    fpath = os.path.join(os.path.abspath(__file__), fname)
    make_file.delay(fpath, content)
    return f"find your file @ <code>{fpath}</code>"