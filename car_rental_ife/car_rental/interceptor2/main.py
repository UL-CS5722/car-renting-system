# encoding=utf8
from interceptorManager import InterceptorManager 
from loggingInterceptor import LoggingInterceptor
from authorisationInterceptor import AuthorisationInterceptor 
from randomInterceptor import RandomInterceptor 
from application import Application 

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