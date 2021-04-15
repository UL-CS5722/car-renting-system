import abc

class Station(metaclass=abc.ABCMeta):
    def __init__(self):
        self._name = None
        self._code = None
        self._address = None
        self._email = None
        self._phone = None

    ##setters
    def set_name(self, name):
        self._name = name

    def set_code(self, code):
        self._code = code

    def set_address(self, address):
        self._address = address

    def set_email(self, email):
        self._email = email

    def set_phone(self, phone):
        self._phone = phone

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