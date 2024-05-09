from flask_restx import Resource, Api
from flask import Blueprint, request
from flask_jwt_extended import jwt_required

from flaskblog.blog.service import BlogOperations

blog_router = Blueprint('Blog', __name__)
blog_api = Api(blog_router, prefix='/blog')


class AllBlogs(Resource):

    @jwt_required()
    def get(self):
        """
        List of all Blogs.
        :return: blog details
        """
        blog_operations = BlogOperations(request)
        return blog_operations.get_blogs()


class NewBlog(Resource):
    @jwt_required()
    def post(self):
        """
        Creates a new blog.
        :return: new created blog details
        """
        blog_operations = BlogOperations(request)
        return blog_operations.create_blog()


class SelectedBlog(Resource):
    blog_operations = BlogOperations(request)

    @jwt_required()
    def get(self, blog_id):
        """
        Get Blog
        :param blog_id: integer
        :return: selected blog
        """

        return self.blog_operations.get_selected_blog(blog_id)

    @jwt_required()
    def put(self, blog_id):
        """
        Updates a blog
        :param blog_id: integer
        :return: updated blog details
        """
        return self.blog_operations.get_updated_blog(blog_id)

    @jwt_required()
    def delete(self, blog_id):
        """
        Deletes a specific Blog
        :return: success msg
        """
        return self.blog_operations.delete_user_blog(blog_id)


# blog blueprint API routes
blog_api.add_resource(AllBlogs, '/', endpoint="All blogs")
blog_api.add_resource(NewBlog, '/new', endpoint="Create new blog")
blog_api.add_resource(SelectedBlog, '/<int:blog_id>', endpoint="Select particular blog")
