import copy
from .customer import Customer

class Prototype:
    def __new_customer(self, cust):
        _new = copy.deepcopy(cust)
        return _new

    def clone(self):
        return Prototype().__new_customer(cust=Customer())