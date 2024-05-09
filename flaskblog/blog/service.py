from flask_jwt_extended import get_jwt_identity

from flaskblog import common_language
from flaskblog.blog.model import Post
from flaskblog.blog import language, schemas, constant


class BlogOperations:

    def __init__(self, request):
        self.request = request

    @staticmethod
    def get_blogs():
        """
        select all blogs from db
        :return: json schema response data
        """
        posts = Post.get_posts()
        response_data = language.user_response_many_data(posts, schemas.PostDetailResponseSchema)
        return response_data

    @staticmethod
    def get_selected_blog(blog_id):
        """
        select particular blog by blog_id
        :param blog_id: integer
        :return: json blog data
        """

        blog = Post.get_by_id(blog_id)
        if blog:
            response_data = common_language.get_response_data_lang(blog, schemas.PostDetailResponseSchema)
            return common_language.return_response(constant.SELECTED_BLOG_DETAILS_MSG, response_data)
        return common_language.return_response(constant.BLOG_NOT_EXIST, )

    @staticmethod
    def delete_user_blog(blog_id):
        """
        delete blog
        :param blog_id: integer
        :return: json success msg or error
        """

        blog = Post.get_by_id(blog_id)
        if blog:
            user_id = get_jwt_identity()
            if blog.user_id == user_id:
                blog.delete()
                return common_language.return_response(constant.BLOG_DELETE_MSG, )
            return common_language.return_response(constant.NO_ACCESS_ENDPOINT_MSG, )
        return common_language.return_response(constant.BLOG_NOT_EXIST, )

    def create_blog(self):
        """
        create new blog
        :return: json new created data or error
        """

        error, post_data = common_language.get_req_data_lang(self.request, schemas.PostDetailRequestSchema)
        if not error:
            user_id = get_jwt_identity()
            post_data['user_id'] = user_id

            post = Post(post_data)
            post.save()
            response_data = common_language.get_response_data_lang(post, schemas.PostDetailResponseSchema)
            return common_language.return_response(constant.BLOG_CREATED_MSG, response_data)
        return post_data

    def get_updated_blog(self, blog_id):
        """
        update existed blog
        :param blog_id: integer
        :return: updated blog json data or error message
        """

        error, post_data = common_language.get_req_data_lang(self.request, schemas.PostUpdateRequestSchema)
        if not error:
            user_id = get_jwt_identity()
            blog = Post.get_by_id(blog_id)
            if blog:
                if blog.user_id == user_id:
                    updated_blog = blog.update(post_data)
                    response_data = common_language.get_response_data_lang(updated_blog, schemas.PostDetailResponseSchema)
                    return common_language.return_response(constant.BLOG_UPDATE_MSG, response_data)
                return common_language.return_response(constant.NO_ACCESS_ENDPOINT_MSG, )
            return common_language.return_response(constant.BLOG_NOT_EXIST, )
        return post_data
