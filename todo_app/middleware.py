def simple_middleware(get_response):
    def middleware(request):
        print("before response")
        response = get_response(request)
        print("After response")
        return response
    return middleware


class SimpleMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
    def __call__(self, request):
        print("before response")
        response = self.get_response(request)
        print("After response")
        return response

class SimpleMiddlewareStructure:
    def _init_(self, get_response):
        self.get_response = get_response
    def _call_(self, request):
        response = self.get_response(request)
        return response
    def process_view(self, request, view_func, view_args, view_kwargs):
        pass
    def process_exception(self, request, exception):
        pass
    def process_template_response(self, request, response):
        return response