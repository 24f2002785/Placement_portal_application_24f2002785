from flask import Flask
from extensions import db, login_manager


def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = 'placement-secret-2024'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///placement.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    login_manager.init_app(app)

    return app


if __name__ == '__main__':
    app = create_app()
    with app.app_context():
        from models import db as _db
        _db.create_all()
    app.run(debug=True)