from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from flask_marshmallow import Marshmallow
from flask_jwt_extended import JWTManager
from flask_mail import Mail

from config import Config

db = SQLAlchemy()
marshmallow = Marshmallow()
bcrypt = Bcrypt()
migrate = Migrate()
jwt_manager = JWTManager()
mail = Mail()


def create_app():
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object(Config)

    # initializing app
    db.init_app(app)
    marshmallow.init_app(app)
    migrate.init_app(app, db)
    bcrypt.init_app(app)
    jwt_manager.init_app(app)
    mail.init_app(app)

    with app.app_context():
        from flaskblog.user.route import user_router
        from flaskblog.blog.route import blog_router

        # register blueprint

        app.register_blueprint(blog_router)
        app.register_blueprint(user_router)

        return app
