from __future__ import annotations
from abc import ABC, abstractmethod
from datetime import datetime

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

    def to_str(self, cars):
        self._car= ' '.join([str(elem) for elem in cars])
        return self._car

    def to_lst(self, cars):
        self._car= cars.split()
        return self._car


class Originator():
    _state = None

    def __init__(self, state) -> None:
        self._state = state
        print(f"Originator: My initial state is: {self._state}")

    def new_state(self, state) -> None:
        self._state = state

    def save(self) -> Memento:
        return ConcreteMemento(self._state)

    def restore(self, memento: Memento) -> None:

        self._state = memento.get_state()
        print(f"Originator: My state has changed to: {self._state}")

class Memento(ABC):

    @abstractmethod
    def get_name(self) -> str:
        pass

    @abstractmethod
    def get_date(self) -> str:
        pass


class ConcreteMemento(Memento):
    def __init__(self, state) -> None:
        self._state = state
        self._date = str(datetime.now())[:19]
        
    def get_state(self):
        return self._state

    def get_name(self):
        return f"{self._state[0:100]}"

    def get_date(self) -> str:
        return self._date


class Caretaker():
    def __init__(self, originator: Originator) -> None:
        self._mementos = []
        self._originator = originator

    def backup(self) -> None:
        print("\nCaretaker: Saving Originator's state...")
        self._mementos.append(self._originator.save())

    def undo(self) :
        if not len(self._mementos):
            return

        memento = self._mementos.pop()
        prev = memento.get_name()
        return prev
        #print(f"Caretaker: Restoring state to: {memento.get_name()}")
        try:
            self._originator.restore(memento)
        except Exception:
            self.undo()

    def show_history(self) -> None:
        print("Caretaker: Here's the list of mementos:")
        for memento in self._mementos:
            print(memento.get_name()) 

if __name__ == "__main__":

    '''Create a new wishlist'''
    wishlist = Wishlist()
    wishlist.add_car("Honda_2019")
    wishlist.add_car("Toyota_2019")
    wishlist.add_car("Ford_2020")

    cars = wishlist.get_car()
    newstate = wishlist.to_str(cars) #Convert to list to string


    originator = Originator(newstate)
    caretaker = Caretaker(originator)
    caretaker.backup()   #Save state
    caretaker.show_history()  #Show history of saved states

    wishlist.add_car("Benz_2020")    #Add a new car to the list
    newstate = wishlist.to_str(cars)    #Convert to list to string
    originator.new_state(newstate)    #Create a new state

    caretaker.backup()   #Save state
    caretaker.show_history()  #Show history of saved states

    wishlist.add_car("Ford_2010")   #Add a new car to the list
    newstate = wishlist.to_str(cars)   #Convert to list to string'''
    originator.new_state(newstate)      

    caretaker.backup()  #Save state'''
    caretaker.show_history()  #Show history of saved states'''

    wishlist.remove("Benz_2020")   #remove an item from the list''' 

    '''Undo wishlist'''
    prev =  caretaker.undo()
    prev_lst = wishlist.to_lst(prev)
    wishlist.set_car(prev_lst)
    cars = wishlist.get_car()
    print(cars)
   
    #wishlist.add_car("Test_2010")

