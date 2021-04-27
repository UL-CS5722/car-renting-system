class Address:
    def __init__(self, street, city, postcode, country='Ireland'):
        self._street = street
        self._city = city
        self._postcode = postcode
        self._country = country

    ##setters
    def set_street(self, street):
        self._street = street

    def set_city(self, city):
        self._city = city

    def set_postcode(self, postcode):
        self._postcode = postcode

    def set_country(self, country):
        self._country = country

    ##getters
    def get_street(self):
        return self._street

    def get_city(self):
        return self._city

    def get_postcode(self):
        return self._postcode

    def get_country(self):
        return self._country

    def __repr__(self):
        return f"{self._street}, {self._city}, {self._postcode}, {self._country}"

    # def __str__(self):
    #     return f"{self._street_address}, {self._city}, {self._postcode}, {self._country}"