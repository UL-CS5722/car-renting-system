# encoding=utf8
import logging
from interceptor import Interceptor


#class LoggingInterceptor(Interceptor): 
    #def execute(self, request): 
        #print("In the logging interceptor!")

messages = []
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


class ListenFilter(logging.Filter):

    def filter(self, record):
        """Determine which log records to output.
        Returns 0 for no, nonzero for yes.
        """
        if record.getMessage().startswith('dont: '):
            return False
        return True


class RequestsHandler(logging.Handler):
    def emit(self, record):
        """Send the log records (created by loggers) to
        the appropriate destination.
        """
        messages.append(record.getMessage())


handler = RequestsHandler()
logger.addHandler(handler)

filter_ = ListenFilter()
logger.addFilter(filter_)

# log I want
logger.info("logme: Howdy!")


# log i want to skip
logger.info("dont: I'm doing great!")

# prints ['logme: Howdy!']
print(messages)        