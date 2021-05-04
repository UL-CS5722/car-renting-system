import unittest
from datetime import datetime
from ..booking import Booking


class TestBooking(unittest.TestCase):

    def test_new_booking(self):
        # arrange
        date = datetime.now()

        # act
        booking = Booking()
        booking.new(station_code='CRK', booking_date=date)

        # assert
        self.assertEqual(booking._booked_at, 'CRK')
        self.assertEqual(booking._booked_for, date)
        self.assertEqual(booking._booking_id[0], "b")
        self.assertEqual(booking._booking_id[1:4], "crk")  
        self.assertTrue(booking._booking_id[4:].isdigit())

    def test_delete_booking(self):
        booking = Booking()

        # arrange
        booking_dict = { "bcrk2": booking }

        # act
        result = booking.delete(booking_dict, "bcrk4")

        # assert
        self.assertTrue(result, 'Not a valid booking ID!')
