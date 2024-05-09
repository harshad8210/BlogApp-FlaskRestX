from flask_jwt_extended import get_jwt_identity

from flaskblog import common_language
from flaskblog.user.model import User
from flaskblog.user import schemas, utils, constant
from flaskblog.user.utils import ResetPasswordSendMail
from flaskblog.user.validation import check_hash_password


class UserOperation:

    def __init__(self, request):
        self.request = request

    def create_new_user(self):
        """
        Function creates new user
        :return: schema response data or error
        """

        error, req_data = common_language.get_req_data_lang(self.request, schemas.UserRegisterRequestSchema)
        if not error:
            username = req_data.get('username', None)
            email = req_data.get('email', None)
            password = req_data.get('password', None)

            existed_username = User.username_exist(username)
            if existed_username is None:
                existed_email = User.user_email_exist(email)
                if existed_email is None:
                    hash_password = utils.convert_pass_hash(password)
                    req_data['password'] = hash_password
                    user = User.create_new_user(req_data)

                    response_data = common_language.get_response_data_lang(user, schemas.UserRegisterResponseSchema)
                    return common_language.return_response(constant.USER_ACC_CREATED_MSG, response_data)
                return common_language.return_response(constant.EMAIL_EXISTS_MSG, )
            return common_language.return_response(constant.USER_EXISTS_MSG, )
        return req_data

    def login_user(self):
        """ log in user and create access and refresh token
        :return: schema response data or error message
        """

        error, req_data = common_language.get_req_data_lang(self.request, schemas.UserLoginRequestSchema)
        if not error:
            email = req_data.get('email')
            password = req_data.get('password')

            user = User.user_email_exist(email)
            if user is not None:
                if check_hash_password(user.password, password):
                    access_token, refresh_token = utils.generate_access_refresh_token(user.id)

                    response_data = common_language.get_response_data_lang(user, schemas.UserRegisterResponseSchema)
                    response_data['access_token'] = access_token
                    response_data['refresh_token'] = refresh_token

                    return common_language.return_response(constant.USER_SUCCESS_LOGIN_MSG, response_data)
                return common_language.return_response(constant.USER_PASS_NOT_VALID_MSG, )
            return common_language.return_response(constant.USER_EMAIL_NOT_VALID_MSG, )
        return req_data

    def change_user_pass(self):
        """
        change user password
        :return: error or success message
        """

        error, req_data = common_language.get_req_data_lang(self.request, schemas.UserChangePasswordSchema)
        if not error:
            current_password = req_data.get('current_password', None)
            new_password = req_data.get('new_password', None)
            confirm_password = req_data.get('confirm_password', None)
            if new_password == confirm_password:
                user_id = get_jwt_identity()
                user = User.get_user_by_id(user_id)
                if check_hash_password(user.password, current_password):
                    new_password = utils.convert_pass_hash(new_password)
                    user.change_password(new_password)
                    return common_language.return_response(constant.USER_PASS_SUCCESS_CHANGE_MSG, )
                return common_language.return_response(constant.INCORRECT_CURRENT_PASS_MSG, )
            return common_language.return_response(constant.INCORRECT_CONFIRM_PASS_MSG, )
        return req_data

    def forgot_user_password(self):
        """
        send forgot password url to user mail
        :return: message
        """

        error, req_data = common_language.get_req_data_lang(self.request, schemas.UserForgotPassSchema)
        if not error:
            user_email = req_data.get('email', None)
            user = User.user_email_exist(user_email)
            if user:
                token = utils.generate_email_token(user.id)
                reset_pass_send_mail = ResetPasswordSendMail(token)
                if reset_pass_send_mail.send_mail_forgot_pass(user.email, self.request.host_url):
                    return common_language.return_response(constant.SUCCESS_MAIL_SEND_MSG, )
                return common_language.return_response(constant.INTERNAL_SERVER_ERROR_MSG, )
            return common_language.return_response(constant.EMAIL_VALIDATION_ERROR_MSG, )
        return req_data

    def reset_user_password(self, token):
        """
        reset password with valid token
        :param token: hashed token
        :return: message
        """

        error, req_data = common_language.get_req_data_lang(self.request, schemas.UserResetPassSchema)
        if not error:
            reset_pass_send_mail = ResetPasswordSendMail(token)
            user_id = reset_pass_send_mail.get_decode_token()
            user = User.get_user_by_id(user_id)
            if user:
                new_password = req_data.get("password")
                new_hash_password = utils.convert_pass_hash(new_password)
                user.change_password(new_hash_password)
                return common_language.return_response(constant.USER_PASS_SUCCESS_RESET_MSG, )
            return common_language.return_response(constant.USER_EXISTS_MSG, )
        return req_data
