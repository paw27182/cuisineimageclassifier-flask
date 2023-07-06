from pathlib import Path

from flask import Blueprint, redirect, render_template

topview_bp = Blueprint('topview_bp', __name__,
                       template_folder='templates/topview',
                       static_url_path='/topview/static',
                       static_folder='../topview/static',
                       )


@topview_bp.route("/", methods=["GET"])
def index():
    return redirect("/topview")


@topview_bp.route("/topview")
def topview():
    headline = "Cuisine Image Classifier"
    return render_template("topview.html",
                           headline=headline,
                           )
