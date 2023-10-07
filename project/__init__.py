from flask import Flask 
from flask_sqlalchemy import SQLAlchemy

#Initialize SQLAlchemy
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = 'A-VERY-SECRET-KEY'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sqlite.db'

    db.init_app(app)

    from .models import User
    
    with app.app_context():
        db.create_all()

    # blueprint for auth routes in app
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    # blueprint for non auth routes
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
