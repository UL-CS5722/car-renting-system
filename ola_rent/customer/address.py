class Address:
    def __init__(self, street_address, city, postcode, country):
        self._street_address = street_address
        self._city = city
        self._postcode = postcode
        self._country = country

    def __repr__(self):
        return f"{self._street_address}, {self._city}, {self._postcode}"

    def __str__(self):
        return f"{self._street_address}, {self._city}, {self._postcode}"
