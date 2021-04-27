from ..utils import logger

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
        self._builder._build_id()
        logger.info(f"{self._builder._car._company} company car with ID: {self._builder._car._id} is built!")

    def get_car(self):
        return self._builder.get_car()


    
