class Director():

    def __init__(self, builder):
        self._builder = builder

    def construct_car(self):
        self._builder.create_new_car()
        self._builder.add_model()
        self._builder.add_seats()
        self._builder.add_geartype()

    def get_car(self):
        return self._builder.car
