from .vehicle import Vehicle

class Jeep(Vehicle):
    """Product"""
    model = None
    gear_type = None
    def __init__(self, model=model, gear_type=gear_type):
        super().__init__()
        self.model = model
        self.gear_type = gear_type
    
    def __str__(self):
        return f"Car class created with Gear type: {self.gear_type}"
