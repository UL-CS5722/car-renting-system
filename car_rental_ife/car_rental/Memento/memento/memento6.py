from __future__ import annotations
from abc import ABC, abstractmethod
from datetime import datetime
from random import sample
from string import ascii_letters, digits
import re

car= None
carlist = list()

class Wishlist():
    def __init__(self):
         self._car_list = carlist
      
    # getter method
    def get_car(self):
        return self._car_list
      
    # setter method
    def set_car(self, new_car):
        self._car_list = new_car
    
    def add_car(self, new_car):
        self._car = new_car
        carlist.append(self._car)
        print(f"A new car has been added to your wishlist: {carlist}")

    def remove(self, new_car):
        self._car = new_car
        carlist.remove(self._car) 
        print(f"a car has been removed from your wishlist: {carlist}")
class Memento():  # pylint: disable=too-few-public-methods
    "A container of state"
    def __init__(self, state):
        self.state = state
class Originator():
    "The Object in the application whose state changes"
    def __init__(self):
        self._state = ""
    @property
    def state(self):
        "A `getter` for the objects state"
        return self._state
    @state.setter
    def state(self, state):
        print(f"Originator: Setting state to `{state}`")
        self._state = state
    @property
    def memento(self):
        "A `getter` for the objects state but packaged as a Memento"
        print("Originator: Providing Memento of state to caretaker.")
        return Memento(self._state)
    @memento.setter
    def memento(self, memento):
        self._state = memento.state
        print(
            f"Originator: State after restoring from Memento: "
            f"`{self._state}`")
class CareTaker():
    "Guardian. Provides a narrow interface to the mementos"
    def __init__(self, originator):
        self._originator = originator
        self._mementos = []
    def create(self):
        "Store a new Memento of the Originators current state"
        print("CareTaker: Getting a copy of Originators current state")
        memento = self._originator.memento
        self._mementos.append(memento)
    def restore(self, index):
        """
        Replace the Originators current state with the state
        stored in the saved Memento
        """
        print("CareTaker: Restoring Originators state from Memento")
        memento = self._mementos[index]
        self._originator.memento = memento
        return self._originator.memento

if __name__ == "__main__":
    # The Client
    ORIGINATOR = Originator()
    CARETAKER = CareTaker(ORIGINATOR)
    # originators state can change periodically due to application events

    wishlist = Wishlist()
    wishlist.add_car("Honda_2019")
    wishlist.add_car("Toyota_2019")
    wishlist.add_car("Ford_2020")

    cars = wishlist.get_car()
    new_state = ' '.join([str(elem) for elem in cars])
    print(new_state)

    ORIGINATOR.state = new_state
    CARETAKER.create()
    print(ORIGINATOR.state)

    wishlist.add_car("Benz_2020")
    new_state = ' '.join([str(elem) for elem in cars])
    print(new_state)

    ORIGINATOR.state = new_state
    CARETAKER.create()
    print(ORIGINATOR.state)

    CARETAKER.restore(0)
    #mystr = 'This is a string, with words!'
    #wishlist = re.sub("[^\w]", " ",  undo).split()
    print(wishlist)


    '''ORIGINATOR.state = "State #2"
    # lets backup the originators
    CARETAKER.create()
    # more changes, and then another backup
    ORIGINATOR.state = "State #3"
    CARETAKER.create()
    # more changes
    ORIGINATOR.state = "State #4"
    print(ORIGINATOR.state)
    # restore from first backup
    CARETAKER.restore(0)
    print(ORIGINATOR.state)
    # restore from second backup
    CARETAKER.restore(1)
    print(ORIGINATOR.state)'''