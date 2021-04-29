from ..customer import Customer
from ..vehicles import Car
from random import randint
from ..utils import logger

class Booking():
    """
    Booking Class that defines the booking process
    """
    def __init__(self):
        self._booking_id = None
        self._customer_id = Customer()

    def new(self, station_code, booking_date):
        self._car_id = Car()._id
        self._booked_at = station_code
        self._booked_for = booking_date
        self._booking_id = "b" + self._booked_at.lower() + str(randint(0, 100))
        logger.info(f"New order with id: {self._booking_id} is generated.")
        return self._booking_id

    def update(self, booking_id):
        return self.new(self._booked_at, self._booked_for)
        

    def delete(self, booking_dict, booking_id):
        if booking_id in booking_dict:
            del booking_dict[booking_id]
            return f'Booking ID: {booking_id} is deleted'
        return 'Not a valid booking ID!'

    def __repr__(self):
        return f"A booking object with id {self._booking_id} is created!"
