from django.http import HttpRequest


class CorsMiddle:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request: HttpRequest):
        response = self.get_response(request)
        if request.method == "OPTIONS":
            response["Access-Control-Allow-Headers"] = 'x-csrftoken'
            response["Access-Control-Allow-Methods"] = "POST,GET,PUT,OPTIONS"
            response["Access-Control-Max-Age"] = 3600
            response["Access-Control-Allow-Origin"] = "*"
            return response
        else:
            return response