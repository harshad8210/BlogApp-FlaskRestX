from flaskblog import db
from sqlalchemy.exc import IntegrityError, SQLAlchemyError
from flaskblog.blog.model import Post


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref='author')

    def __init__(self, data):
        self.username = data.get('username')
        self.email = data.get('email')
        self.password = data.get('password')

    def __repr__(self):
        return f"User('{self.username}','{self.email}')"

    def save(self):
        try:
            db.session.add(self)
            db.session.commit()
        except IntegrityError as error:
            db.session.rollback()
            raise error
        except SQLAlchemyError as error:
            db.session.rollback()
            raise error

    def change_password(self, new_password):
        """
        change user password
        :param new_password: string (hashed password)
        :return: NULL
        """
        self.password = new_password
        db.session.commit()

    @classmethod
    def user_email_exist(cls, email):
        """
        Find the existing user with email
        :param email: string
        :return: user or None
        """
        user = cls.query.filter_by(email=email).first()
        return user

    @classmethod
    def username_exist(cls, username):
        """
        find the existing user with username
        :param username: string
        :return: user or None
        """
        user = cls.query.filter_by(username=username).first()
        return user

    @classmethod
    def get_user_by_id(cls, id):
        """
        find the existing user with user id
        :param id: integer
        :return: user or None
        """
        user = cls.query.filter_by(id=id).first()
        return user

    @classmethod
    def create_new_user(cls, data):
        """
        create new user
        :param data: user data in json
        :return: new user
        """
        user = cls(data)
        user.save()
        return user
