# encoding=utf8
from interceptor import Interceptor
class AuthorisationInterceptor(Interceptor): 
    def execute(self, request): 
        print("In the authorisation interceptor!")