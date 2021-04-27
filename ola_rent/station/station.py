import abc
from ..customer.address import Address

class Station(metaclass=abc.ABCMeta):
    def __init__(self):
        self._name = None
        self._code = None
        self._address = Address('', '', '')
        self._email = None
        self._phone = None

    ##setters
    @abc.abstractmethod
    def set_name(self, name):
        pass

    @abc.abstractmethod
    def set_code(self, code):
        pass

    @abc.abstractmethod
    def set_address(self, address):
        pass

    @abc.abstractmethod
    def set_email(self, email):
        pass

    @abc.abstractmethod
    def set_phone(self, phone):
        pass

    @abc.abstractmethod
    def create_station(self):
        pass
    
    ##getters
    def get_name(self):
        return self._name

    def get_code(self):
        return self._code

    def get_address(self):
        return self._address

    def get_email(self):
        return self._email

    def get_phone(self):
        return self._phone