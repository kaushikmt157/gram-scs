from flask import Blueprint

pages_bp = Blueprint("pages", __name__)

@pages_bp.route("/test-page")
def test_page():
    return "Pages blueprint working"
