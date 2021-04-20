class Customer():
    def __init__(self):
        self._name = None
        self._address = None
        self._email = None
        self._phone = None
        self._member_type = None
    
    def create(self, name, address, email, phone, member_type):
        self.set_name(name)
        self.set_address(address)
        self.set_email(email)
        self.set_phone(phone)
        self.set_member_type(member_type)
        return self

    ##Setters      
    def set_name(self, name):
        self._name = name

    def set_address(self, address):
        self._address = address

    def set_email(self, email):
        self._email = email

    def set_phone(self, phone):
        self._phone = phone
    
    def set_member_type(self, member_type='Basic'):
        self._member_type = member_type

    
    ##Getters
    def get_name(self):
        return self._name

    def get_address(self):
        return self._address

    def get_email(self):
        return self._email

    def get_phone(self):
        return self._phone

    def get_member_type(self):
        return self._member_type

    def __repr__(self):
        return f"Name: {self._name}\nAddress: {self._address}\nType: {self._member_type}"
    