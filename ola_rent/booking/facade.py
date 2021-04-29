from .booking import Booking
from .status import Status

class Facade():

    def __init__(self):
        self.booking1 = Booking()
        self.status = Status()

    def operations(self, station_code, booking_date):
        b_id = self.booking1.new(station_code, booking_date)
        self.status.booked()
        return b_id
