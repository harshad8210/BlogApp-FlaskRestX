from flaskblog import bcrypt, mail
from flask_mail import Message
import datetime
from flask_jwt_extended import create_access_token, create_refresh_token, decode_token


def convert_pass_hash(password):
    """
    convert plain password to confirm password
    :param password:
    :return: hashed password
    """
    hash_pass = bcrypt.generate_password_hash(password).decode('utf-8')
    return hash_pass


def generate_access_refresh_token(user_id):
    """
    generates JWT access token and refresh token
    :param user_id: integer
    :return: access token, refresh token
    """

    access_token = create_access_token(identity=user_id)
    refresh_token = create_refresh_token(identity=user_id)
    return access_token, refresh_token


def generate_email_token(user_id):
    """
    generates email token using jwt create access token
    :param user_id: integer
    :return: hashed token(string)
    """

    token_exp_time = datetime.timedelta(minutes=30)
    password_reset_token = create_access_token(user_id, expires_delta=token_exp_time)
    return password_reset_token


class ResetPasswordSendMail:

    def __init__(self, token):
        self.token = token

    def get_decode_token(self):
        """
        decode email jwt access token
        :param token: token
        :return: user id
        """
        user_id = decode_token(self.token)['sub']
        return user_id

    def get_mail_message_body(self, host_url):
        """
        email body
        :param token: string
        :param host_url: host url
        :return: msg body
        """

        msg_body = f"""
    To reset your password, visit the following link:{host_url}user/reset-password/{self.token}
    If you did not make this request then simply ignore this email and no changes will be made.
    """
        return msg_body

    def send_mail_forgot_pass(self, user_email, host_url):
        """
        send mail to user email
        :param user_email: string
        :param token: string
        :param host_url: host url
        :return: mail send(True) or not(False)
        """

        try:
            msg = Message('Password Reset Request', sender='inexture@gmail.com', recipients=[user_email])
            msg.body = self.get_mail_message_body(host_url)
            mail.send(msg)
            return True

        except Exception as e:
            return False
