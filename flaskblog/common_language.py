from flask import jsonify
from marshmallow import ValidationError


def get_req_data_lang(request, schema):
    """
    load requested schema
    :param request: schema request data
    :param schema: schema
    :return: error checked(True/False) and error msg/json data
    """

    data = request.get_json()
    try:
        post_data = schema().load(data)
        return False, post_data
    except ValidationError as error:
        return True, error.messages


def get_response_data_lang(data, schema):
    """
    create response data
    :param data: response data
    :param schema: schema
    :return: json data
    """
    response_data = schema().dump(data)
    return response_data


def return_response(message=None, data=None):
    """
    generate json data response
    :param message: string
    :param data: response data of schema
    :return: json data
    """
    return jsonify({"message": message}, data)
