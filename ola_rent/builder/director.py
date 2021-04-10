class Director:
    """
    Construct an object using the Builder Interface
    """
    def __init__(self, builder):
        self._builder = builder

    def build_car(self):
        self._builder.new_car()
        self._builder._build_seats()
        self._builder._build_model()
        self._builder._build_gear()
        self._builder._build_company()
        self._builder._build_year()

    def get_car(self):
        return self._builder.get_car()


    
