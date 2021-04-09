class Director():

    def __init__(self, builder):
        self._builder = builder

    def construct_car(self):
        self._builder.create_new_car()
        # self._builder.generate_vid()
        self._builder.add_seat()
        self._builder.add_company()
        self._builder.add_build_year()
        self._builder.add_mileage()
        self._builder.add_model()
        self._builder.add_gear_type()

    def get_car(self):
        return self._builder.car

    def construct_jeep(self):
        self._builder.create_new_car()
        # self._builder.generate_vid()
        self._builder.add_seat()
        self._builder.add_company()
        self._builder.add_build_year()
        self._builder.add_mileage()
        self._builder.add_model()
        self._builder.add_gear_type()
