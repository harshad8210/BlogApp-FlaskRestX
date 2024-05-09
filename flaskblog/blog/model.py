from flaskblog import db
from flask import jsonify
from datetime import datetime
from sqlalchemy.exc import SQLAlchemyError, IntegrityError


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __init__(self, data):
        self.title = data.get('title')
        self.content = data.get('content')
        self.date_posted = datetime.utcnow()
        self.user_id = data.get('user_id')

    def __repr__(self):
        return f"Post('{self.title}','{self.content}','{self.date_posted}')"

    def save(self):
        try:
            db.session.add(self)
            db.session.commit()
        except IntegrityError as error:
            db.session.rollback()
            raise jsonify(error)
        except SQLAlchemyError as error:
            db.session.rollback()
            raise error

    def update(self, data):
        try:
            for key, item in data.items():
                setattr(self, key, item)
            db.session.commit()
            return self
        except IntegrityError as error:
            db.session.rollback()
            raise error
        except SQLAlchemyError as error:
            db.session.rollback()
            raise error

    def delete(self):
        try:
            db.session.delete(self)
            db.session.commit()
        except IntegrityError as error:
            db.session.rollback()
            raise error
        except SQLAlchemyError as error:
            db.session.rollback()
            raise error

    @classmethod
    def get_posts(cls):
        """class method of Post
        fetch all posts from db
        :return: posts
        """

        posts = cls.query.all()
        return posts

    @classmethod
    def get_by_id(cls, id):
        """
        fetch post by post_id
        :param id:
        :return:
        """

        return cls.query.filter_by(id=id).first()
