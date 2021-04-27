import copy
from .customer import Customer
from ..utils import logger

class Prototype:
    def __new_customer(self, cust):
        _new = copy.deepcopy(cust)
        return _new

    def clone(self):
        logger.info("New customer is created!")
        return Prototype().__new_customer(cust=Customer())