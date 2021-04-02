class Car():
    """Product"""
    def __init__(self):
        self.model = None
        self.seats = None
        self.geartype = None

    def __str__(self):
        return f"Model: {self.model} \nSeat Count: {self.seats} \nGear Type: {self.geartype}"
