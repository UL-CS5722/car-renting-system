from __future__ import annotations
from abc import ABC, abstractmethod
from datetime import datetime
import uuid


class Book():
    __slots__ = ['book_id', 'cust_id', 'car_id', 'date', 'timeslot', 'state', 'price']
    
    def __init__(self, default_value=0):
        for attribute in self.__slots__:
            setattr(self, attribute, default_value)

    def __getitem__(self, key):
        return getattr(self, key)

    def __setitem__(self, key, value):
        setattr(self, key, value)
        self.book_id = self._generate_bookid()
        #self.cust_id = self.get_custid()
        self.date = str(datetime.now())[:19]
        self.state = self._get_status()

    def __iter__(self):
        return iter(self.__slots__)

    def items(self):
        for attribute in self.__slots__:
            yield attribute, getattr(self, attribute)

    def __delattr__(self, key):
        raise AttributeError(key)

    def _generate_bookid(self):
        return uuid.uuid1()
    
    def get_custid(self):
        #return cust_id
        pass

    def get_timeslot(self, timeslot):
        return timeslot
    
    def _get_status(self):
        self.state = Available()
        return self.state

    def change_status(self, state):
        """ Change state """
        return self.state.switch(state)

class Status():
    name = "state"
    allowed = []

    def switch(self, state):
        """ Switch to new state """
        if state.name in self.allowed:
            print('Current:',self,' => switched to new state',state.name)
            self.__class__ = state
        else:
            print('Current:',self,' => switching to',state.name,'not possible.')

    def __str__(self):
        return self.name
    
class Available(Status):
    """Customer initial reservation"""
    name = "available"
    allowed = ['booked']

class Booked(Status):
    """Customer initial reservation"""
    name = "booked"
    allowed = ['pickup', 'cancelled']

class Pickup(Status):
    """ Customer has taken the car from station"""
    name = "pickup"
    allowed = ['returned']

class Returned(Status):
    """ Customer has dropped off from the station """
    name = "returned"
    allowed = ['available']

class Cancelled(Status):
    name = "cancelled"
    allowed = ['available']

if __name__ == "__main__":
    b = Book()
    b['cust_id'] = 6
    b['car_id'] = 3
    b['timeslot'] = '10:30 to 11:00'
    b['price'] = 300
    b.change_status(Booked)

    print(b.cust_id,b.car_id, b.book_id, b.date, b.state, b.price)


