from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

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

    migrate = Migrate(app, db)

    # adding the login manager
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))
    
    return app
