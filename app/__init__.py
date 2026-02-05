from flask import Flask

def create_app():
    app = Flask(__name__)

    from app.main.routes import main_bp
    from app.pages.routes import pages_bp

    app.register_blueprint(main_bp)
    app.register_blueprint(pages_bp)

    return app
