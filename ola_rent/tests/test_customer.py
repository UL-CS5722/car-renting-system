import unittest
from ..customer import Customer, Address


class TestAddress(unittest.TestCase):

    def test_create_customer(self):
        # arrange
        customer = Customer()
        address = Address("67 O'Connell's Street", "Galway", "K94 HU90")

        # act
        customer.create("John", address, "John.doe@olarent.com", 5634654765, "Basic")

        # assert
        self.assertEqual(customer._name, 'John')
        self.assertEqual(customer._address, address)
        self.assertEqual(customer._email, "John.doe@olarent.com")
        self.assertEqual(customer._phone, 5634654765)
        self.assertEqual(customer._member_type, "Basic")

