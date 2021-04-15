from .vehicle import Vehicle

class Car(Vehicle):
    def __init__(self):
        super().__init__()
        self._model = None
        self._gear_type = None

    def __repr__(self):
        return f"Company: {self._company}\nYear: {self._year}\nSeats: {self._seats}\nModel: {self._model}\nGear Type: {self._gear_type}\n"
