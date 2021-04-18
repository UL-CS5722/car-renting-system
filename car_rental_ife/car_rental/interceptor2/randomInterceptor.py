# encoding=utf8
from interceptor import Interceptor
class RandomInterceptor(Interceptor): 
    def execute(self, request): 
        print("In the random interceptor!")