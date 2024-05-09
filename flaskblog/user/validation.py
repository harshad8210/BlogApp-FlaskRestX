import re
from marshmallow import ValidationError

from flaskblog import bcrypt
from flaskblog.user.constant import USERNAME_REGX, EMAIL_REGX, PASSWORD_REGX, USER_VALIDATION_ERROR_MSG, \
    EMAIL_VALIDATION_ERROR_MSG, PASSWORD_VALIDATION_ERROR_MSG


def username_validation(user_name):
    """ validate username with regx
    :param user_name: string
    :return: username or raise validation error
    """
    regex = USERNAME_REGX

    if re.fullmatch(regex, user_name):
        return user_name
    else:
        raise ValidationError(USER_VALIDATION_ERROR_MSG)


def email_validation(email):
    """validate user email with regx
    :param email: string
    :return: email or raise validation error
    """
    regex = EMAIL_REGX

    if re.fullmatch(regex, email):
        return email
    else:
        raise ValidationError(EMAIL_VALIDATION_ERROR_MSG)


def password_validation(password):
    """
    validate user password with regx
    :param password: string
    :return: password or raise validation error
    """

    regex = PASSWORD_REGX

    if re.fullmatch(regex, password):
        return password
    else:
        raise ValidationError(PASSWORD_VALIDATION_ERROR_MSG)


def check_hash_password(data_password, input_password):
    """
    check password is valid or not using bcrypt
    :param data_password: user password stored in db
    :param input_password: plain password/ user input password
    :return: True/False
    """

    checked = bcrypt.check_password_hash(data_password, input_password)
    return checked
