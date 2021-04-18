import copy
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

class Memento(): 
    "A container of state"
    def __init__(self, state):
        self.state = state
        self.idx = 0

    def __iter__ (self):
        return self

    def __next__ (self):
        try:
            item = self.state[self.idx]
        except IndexError:
            raise StopIteration()
        self.idx += 1
        return item

class Originator():
   
    "The Object in the application whose state changes"
    def __init__(self):
        self._state = list()

    @property
    def state(self):
        "A `getter` for the objects state"
        return self._state

    @state.setter
    def state(self, state):
        print(f"Originator: Setting state to `{state}`")
        #self._state = state
        self._state= ' '.join([str(elem) for elem in state])

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
        print("Memento list ",self._mementos)
        print("Originator list ",self._originator)
        print("CareTaker: Getting a copy of Originators current state")
        
        for memento in self._mementos:
            #self._mementos =  self._mementos[:] + memento
            memento = self._originator.memento
            self._mementos.append(memento)

    def restore(self, index):
        """
        Replace the Originators current state with the state
        stored in the saved Memento
        """
        print("CareTaker: Restoring Originators state from Memento")

        #indexs = [list_.index(x) for x in list_]

        memento = self._mementos[index]
        self._originator.memento = memento

    def show_history(self) :
        print("Caretaker: Here's the list of mementos:")
        for memento in self._mementos:
            print(memento)

if __name__ == "__main__":
    ORIGINATOR = Originator()
    CARETAKER = CareTaker(ORIGINATOR)

    wishlist = Wishlist()
    wishlist.add_car("Honda 2019")
    wishlist.add_car("Toyota 2019")
    wishlist.add_car("Ford 2020")

    cars = wishlist.get_car()
    new_state = ' '.join([str(elem) for elem in cars])
    print(new_state)



    # The Client
    
    # originators state can change periodically due to application events
    ORIGINATOR.state = cars
    #ORIGINATOR.state = "State #2"
    # lets backup the originators
    CARETAKER.create()
    wishlist.add_car("Benz 2020")
    # more changes, and then another backup
    ORIGINATOR.state = cars
    CARETAKER.create()
    # more changes
    #ORIGINATOR.state = "State #4"
    print(ORIGINATOR.state)
    # restore from first backup
    #CARETAKER.restore(0)
    print(ORIGINATOR.state)

    #CARETAKER.create()
    #wishlist.add_car("Ford 2010")
    # more changes, and then another backup
   # ORIGINATOR.state = cars
    #CARETAKER.create()
    #print(ORIGINATOR.state)
    # restore from first backup
    #CARETAKER.restore(1)
    #print(ORIGINATOR.state)
    # restore from second backup
    #CARETAKER.restore(1)
    #print(ORIGINATOR.state)