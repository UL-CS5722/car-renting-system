from __future__ import annotations
from abc import ABC, abstractmethod
from datetime import datetime
from random import sample
from string import ascii_letters, digits

carlist = list()
class Wishlist():
    def __init__(self, car_list):
         self._car_list = car_list
      
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

    
    
class Originator():
    _state = None

    def __init__ (self, state: str) -> None:
        self._state = state
        print(f"Originator: My initial state is: {self._state}")

    def add(self, state: str) -> None:

        self._state = self.state(state)
        carlist.append(self._state)
        print(f"A new car has been added to your wishlist: {carlist}")

    def remove(self, state: str) -> None:
        self._state = state
        carlist.remove(self._state) 
        print(f"a car has been removed from your wishlist: {carlist}")

    def state(self, state):
        print(f"New Car added`{state}`")
        self._state = state
        return state


    def save(self) -> Memento:
        """
        Saves the current state inside a memento.
        """

        return ConcreteMemento(self._state)

    def restore(self, memento: Memento) -> None:
        """
        Restores the Originator's state from a memento object.
        """

        self._state = memento.get_state()
        print(f"Originator: My state has changed to: {self._state}")


class Memento(ABC):
    """
    The Memento interface provides a way to retrieve the memento's metadata,
    such as creation date or name. However, it doesn't expose the Originator's
    state.
    """

    @abstractmethod
    def get_name(self) -> str:
        pass

    @abstractmethod
    def get_date(self) -> str:
        pass


class ConcreteMemento(Memento):
    def __init__(self, state: str) -> None:
        self._state = state
        self._date = str(datetime.now())[:19]

    def get_state(self) -> str:
        """
        The Originator uses this method when restoring its state.
        """
        return self._state

    def get_name(self) -> str:
        """
        The rest of the methods are used by the Caretaker to display metadata.
        """

        return f"{self._date} / ({self._state[0:9]}...)"

    def get_date(self) -> str:
        return self._date


class Caretaker():
    """
    The Caretaker doesn't depend on the Concrete Memento class. Therefore, it
    doesn't have access to the originator's state, stored inside the memento. It
    works with all mementos via the base Memento interface.
    """

    def __init__(self, originator: Originator) -> None:
        self._mementos = []
        self._originator = originator

    def backup(self) -> None:
        print("\nCaretaker: Saving Originator's state...")
        self._mementos.append(self._originator.save())

    def undo(self) -> None:
        if not len(self._mementos):
            return

        memento = self._mementos.pop()
        print(f"Caretaker: Restoring state to: {memento.get_name()}")
        try:
            self._originator.restore(memento)
        except Exception:
            self.undo()

    def show_history(self) -> None:
        print("Caretaker: Here's the list of mementos:")
        for memento in self._mementos:
            print(memento.get_name())


if __name__ == "__main__":
    originator = Originator("Honda 2019")
    originator.add("Honda 2019")
    caretaker = Caretaker(originator)

    caretaker.backup()
    originator.add("Toyota 2017")


    caretaker.backup()
    originator.add("Ford 2018")

    caretaker.backup()
    #originator.do_something()

    originator.remove("Ford 2018")

    print()
    caretaker.show_history()

    print("\nClient: Now, let's rollback!\n")
    #caretaker.undo()

    #print("\nClient: Once more!\n")
    #caretaker.undo()