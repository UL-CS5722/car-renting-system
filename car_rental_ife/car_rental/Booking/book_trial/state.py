class CarState(object):
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
    
class Available(CarState):
    """Customer initial reservation"""
    name = "available"
    allowed = ['booked']

class Booked(CarState):
    """Customer initial reservation"""
    name = "booked"
    allowed = ['pickup', 'cancelled']

class Pickup(CarState):
    """ Customer has taken the car from station"""
    name = "pickup"
    allowed = ['returned']

class Returned(CarState):
    """ Customer has dropped off from the station """
    name = "returned"
    allowed = ['available']

class Cancelled(CarState):
    name = "cancelled"
    allowed = ['available']

class Book (object):
    def __init__(self, car_id = 1, customer_id = 1 ):
        self.car_id = car_id
        self.customer_id = customer_id
        # State of the car - default is available.
        self.state = Available()

    def change(self, state):
        """ Change state """
        self.state.switch(state)



if __name__ == "__main__":
    car = Book()
    car.change(Booked)
    car.change(Pickup)
    car.change(Returned)
    car.change(Available)
    car.change(Booked)
    car.change(Cancelled)
    car.change(Available)

 