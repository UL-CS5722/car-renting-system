from .abs_builder import Builder
from enum import Enum

class GearType(Enum):
    AUTOMATIC = 1
    MANUAL = 1


class FordBuilder(Builder):
    
    def _build_seats(self):
        self._car._seats = 6

    def _build_gear(self):
        self._car._gear_type = GearType.AUTOMATIC

    def _build_model(self):
        self._car._model = "A6"

    def _build_company(self):
        self._car._company = "Ford"

    def _build_year(self):
        self._car._year = 2019
