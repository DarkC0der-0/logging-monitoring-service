from flask import Flask
from app.config import Config 
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    with app.app_context():
        from . import routes
        app.register_blueprint(routes.bp)
        db.create_all()

    return app