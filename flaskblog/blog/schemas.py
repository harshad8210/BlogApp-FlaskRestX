from flask_marshmallow.fields import fields
from marshmallow import validate

from flaskblog import marshmallow
from flaskblog.blog.model import Post


class PostDetailResponseSchema(marshmallow.SQLAlchemyAutoSchema):
    class Meta:
        model = Post
        exclude = ('id', 'user_id')


class PostDetailRequestSchema(marshmallow.Schema):
    title = fields.Str(required=True, validate=[validate.Length(min=3, max=50)])
    content = fields.Str(required=True, validate=[validate.Length(min=3, max=100)])


class PostUpdateRequestSchema(marshmallow.Schema):
    title = fields.Str(validate=[validate.Length(min=3, max=50)])
    content = fields.Str(validate=[validate.Length(min=3, max=100)])
