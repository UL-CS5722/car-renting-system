from interceptor import InterceptorManager, LoggingInterceptor, AuthorisationInterceptor, RandomInterceptor, Application
from car_builder import Car, ToyotaBuilder, Director, Builder
from car_clone import Prototype

def main():

    ####Interceptor main
    interceptorManager = InterceptorManager(Application())

    loggingInterceptor = LoggingInterceptor()
    authorisationInterceptor = AuthorisationInterceptor()
    interceptorManager.add(loggingInterceptor)
    interceptorManager.add(authorisationInterceptor)
    interceptorManager.execute("request")

    randomInterceptor = RandomInterceptor()
    interceptorManager.remove(authorisationInterceptor)
    interceptorManager.add(randomInterceptor)
    interceptorManager.execute("request")

    ####Builder main
    builder = ToyotaBuilder()
    director = Director(builder)
    director.construct_car()
    car = director.get_car()
    print(car)

    ####Prototype main
    c = director.get_car()
    prototype = Prototype()
    prototype.register_object("toyota", c)

    c1 = prototype.clone("toyota", 5)

    print(c1)

if __name__ == "__main__":
    main()