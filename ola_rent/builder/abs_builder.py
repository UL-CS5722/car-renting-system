import abc
from .car import Car

class Builder(metaclass=abc.ABCMeta):
    """
    Specify an abstract interface to create parts of the Vehicle
    """
    def __init__(self):
        self._car = None

    def get_car(self):
        return self._car

    def new_car(self):
        self._car = Car()

    @abc.abstractmethod
    def _build_seats(self):
        pass
    
    @abc.abstractmethod
    def _build_model(self):
        pass

    @abc.abstractmethod
    def _build_gear(self):
        pass

    @abc.abstractmethod
    def _build_company(self):
        pass
    
    @abc.abstractmethod
    def _build_year(self):
        pass
