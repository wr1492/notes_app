from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_session import Session

db = SQLAlchemy()
DB_NAME = "study_notes.db"


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'jdf iewjfdka jfd'

    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    app.config["SESSION_PERMANENT"] = False
    app.config["SESSION_TYPE"] = "filesystem"
    Session(app)

    from .auth import auth
    from .models import User, Note

    app.register_blueprint(auth, url_prefix='/')

    with app.app_context():
        db.create_all()

    return app
