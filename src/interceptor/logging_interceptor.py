from .interceptor import Interceptor

class LoggingInterceptor(Interceptor):
    def execute(self, request):
        print("In the Logging Interceptor!")
