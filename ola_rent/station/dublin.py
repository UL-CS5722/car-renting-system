from .station import Station, Address
from ..utils import logger

class Dublin(Station):

    def set_name(self, name='Dublin'):
        self._name = name

    def set_code(self, code='DUB'):
        self._code = code

    def set_address(self, address=''):
        self._address = address

    def set_email(self, email='dublin@olarent.ie'):
        self._email = email

    def set_phone(self, phone='+353 12 345 6789'):
        self._phone = phone

    def create_station(self):
        self.set_name()
        self.set_code()
        self.set_address(Address('Unit 7, Clondalkin', 'Dublin', 'K80 YV61'))
        self.set_email()
        self.set_phone()
        logger.info(f"station {self._name} is created!")

        return self


    def __repr__(self):
        return f"***Station***\nName: {self._name}\nCode: {self._code}\nAddress: {self._address}\nEmail Address: {self._email}\nPhone Number: {self._phone}"
    