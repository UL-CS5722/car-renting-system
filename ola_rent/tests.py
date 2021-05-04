import unittest
from vehicles import Car
from customer import Customer, Address
from booking import Booking
from vehicles import abs_builder, director, ford, hyunday, toyota
from utils import GearType
from datetime import datetime


class TestBookingMethods(unittest.TestCase):
    """
    Test class for the Booking class.
    """
    
    date = datetime.now()
    booking = Booking(station_code='CRK', booking_date=date)
    booking_dict= { booking.id : booking}
    
    def test_new(self):
      """Test the Booking creator method"""
        self.assertEqual(booking.station_code, 'CRK')
        self.assertEqual(booking.booked_for = date)
        self.assertEqual(booking.booking_id[0] , "b")
        self.assertEqual(booking.booking_id[1:3] , "crk")  
        self.assertTrue(booking.booking_id[3:].is_integer())
        
    def test_delete(self):
      """Test the Booking delete method"""
      self.assertTrue(isinstance(booking, booking_dict))
      booking.delete(self, booking_dict, booking.id)
      self.assertFalse(isinstance(booking, booking_dict))
      self.assertTrue(booking.delete(self, booking_dict, booking.id), 'Not a valid booking ID!')

class TestAddressMethods(unittest.TestCase):   
  """
  Test class for the Adress class
  """
  
  address=Address('67 O\'Connell\'s Street', 'Galway', 'K94 HU90')
  
  def test_creator(self):
    """Test the Adress creator method"""
    self.assertEqual(address.name, '67 O\'Connell\'s Street')
    self.assertEqual(address.city, 'Galway')
    self.assertEqual(address.postcode, 'K94 HU90')
    self.assertEqual(address.country, 'Ireland')
    
    
class TestCustomerMethods(unittest.TestCase):
     """
     Test class for the Customer class
     """
    
     address=Address('67 O\'Connell\'s Street', 'Galway', 'K94 HU90')
     customer = Customer().create("John", address, email = "John.doe@olarent.com", phone = 0000000000)
    
     def test_creator(self):
     """Test the Customer creator method"""
     self.assertEqual(customer.name, 'John')
     self.assertEqual(customer.address, address)
     self.assertEqual(customer.email, "John.doe@olarent.com")
     self.assertEqual(customer.phone, 0000000000)
     self.assertEqual(customer.member_type, "basic")

class TestVehicleBuilder(unittest.TestCase):
     """
     Test class for the Builder Pattern in Vehicle
     """
    
    toyota_builder = Director(ToyotaBuilder())
    toyota_builder.build_car()
    toyota = toyota_builder.get_car()
    
    def test_builder(self):
      self.assertEqual(toyota.car.seats,  4)
      self.assertEqual(toyota.car.gear_type, GearType.MANUAL)
      self.assertEqual(toyota.car.model, "G4")
      self.assertEqual(toyota.car.company, "Toyota")
      self.assertEqual(toyota.car.year, "2015")


if __name__ == '__main__':
    unittest.main()
