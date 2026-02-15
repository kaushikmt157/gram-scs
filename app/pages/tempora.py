from flask import Blueprint, render_template, abort

pages_bp = Blueprint(
    "pages",
    __name__,
    template_folder="templates"
)

@pages_bp.route("/<page>")
def show_page(page):
    try:
        return render_template(f"pages/{page}.html")
    except Exception as e:
        print(e)
        abort(404)
