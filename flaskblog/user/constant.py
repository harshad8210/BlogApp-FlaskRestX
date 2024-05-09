# Statics for validations---------------------------

USERNAME_REGX = r"^[A-Za-z\d@$!_#%*?&]{3,30}$"
EMAIL_REGX = r"^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w+$"
PASSWORD_REGX = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{8,16}$"

USER_VALIDATION_ERROR_MSG = "Please enter valid username!"
EMAIL_VALIDATION_ERROR_MSG= "Please enter valid email!"
PASSWORD_VALIDATION_ERROR_MSG = "Please enter valid password!"

# Statics for service-------------------------------------

EMAIL_EXISTS_MSG = "Email is already existed, Please, Try different one...!!!"
USER_EXISTS_MSG = "Username is already existed, Please, Try different one...!!!"
USER_PASS_NOT_VALID_MSG = "User Password Not Valid, Please Try Again...!!!"
USER_EMAIL_NOT_VALID_MSG = "User Email Not Valid, Please Try Again...!!!"
USER_ACC_CREATED_MSG = "Your account has been created."
USER_SUCCESS_LOGIN_MSG = "You are successfully logged in."
USER_PASS_SUCCESS_CHANGE_MSG = "Your password has been changed."
USER_PASS_SUCCESS_RESET_MSG = "Your password has been reset."
INCORRECT_CURRENT_PASS_MSG = "Incorrect current password."
INCORRECT_CONFIRM_PASS_MSG = "Confirm password is not equal to new password."
SUCCESS_MAIL_SEND_MSG = "We send a message in your email with reset password URL."
INTERNAL_SERVER_ERROR_MSG = "Something wants wrong. TRY AGAIN...!!!"
