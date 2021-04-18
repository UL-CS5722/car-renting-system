# encoding=utf8
import logging
import requests
from interceptor import Interceptor


#class LoggingInterceptor(Interceptor): 
    #def execute(self, request): 
        #print("In the logging interceptor!")

try:
    import http.client as http_client
except ImportError:
    # Python 2
    import httplib as http_client
http_client.HTTPConnection.debuglevel = 1

# You must initialize logging, otherwise you'll not see debug output.
logging.basicConfig()
logging.getLogger().setLevel(logging.DEBUG)
requests_log = logging.getLogger("requests.packages.urllib3")
requests_log.setLevel(logging.DEBUG)
requests_log.propagate = True

requests.get('https://google.com')
