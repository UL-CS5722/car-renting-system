from .station import Station

class Galway(Station):

    def set_name(self, name='Galway'):
        self._name = name

    def set_code(self, code='GLY'):
        self._code = code

    def set_address(self, address='67 O\'Connell\'s Street, Galway'):
        self._address = address

    def set_email(self, email='galway@olarent.ie'):
        self._email = email

    def set_phone(self, phone='+353 12 345 6789'):
        self._phone = phone

    def create_station(self):
        self.set_name()
        self.set_code()
        self.set_address()
        self.set_email()
        self.set_phone()

        return self


    def __repr__(self):
        return f"***Station***\nName: {self._name}\nCode: {self._code}\nAddress: {self._address}\nEmail Address: {self._email}\nPhone Number: {self._phone}"
    