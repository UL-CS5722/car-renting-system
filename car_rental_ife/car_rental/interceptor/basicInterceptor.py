# encoding=utf8
class BasicInterceptor:
    def __init__(self, application):
        self.application = application
    def execute(self, request):
        print("In interceptor!")
        self.application.execute(request)