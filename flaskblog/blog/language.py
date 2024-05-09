def user_response_many_data(data, schema):
    """
    create json response with help of schema
    :param data: query fetched data
    :return: json data
    """
    response_data = schema(many=True).dump(data)
    return response_data

