from .builder import Builder

class ToyotaBuilder(Builder):
    """Concrete Builder --> provides parts and tools to work on the parts"""

    def add_model(self):
        self.car.model = "Toyota S4"

    def add_seats(self):
        self.car.seats = "5"

    def add_geartype(self):
        self.car.geartype = "Automatic"
