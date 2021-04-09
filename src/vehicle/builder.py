from .car import Car
from .jeep import Jeep

class Builder():
    """Abstract Builder"""
    def __init__(self):
        self.car = None
        self.jeep = None

    def create_new_car(self):
        self.car = Car()

    def create_new_jeep(self):
        self.jeep = Jeep()