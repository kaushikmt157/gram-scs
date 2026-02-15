from flask import Blueprint, render_template

main_bp = Blueprint(
    "main",
    __name__,
    template_folder="templates"
)

@main_bp.route("/")
def index():
    return render_template("main/index.html")

@main_bp.route("/about")
def about():
    return render_template("main/about.html")

@main_bp.route("/contact")
def contact():
    return render_template("main/contact.html")
