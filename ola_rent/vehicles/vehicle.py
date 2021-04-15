class Vehicle:
    def __init__(self):
        self._company = None
        self._year = None
        self._seats = None

    def __repr__(self) :
        return f"Company: {self._company}\nYear: {self._year}\nSeats: {self._seats}\n"