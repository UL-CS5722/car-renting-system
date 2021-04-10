from .abs_builder import Builder
from enum import Enum

class GearType(Enum):
    AUTOMATIC = 1
    MANUAL = 1


class ToyotaBuilder(Builder):
    
    def _build_seats(self):
        self._car._seats = 4

    def _build_gear(self):
        self._car._gear_type = GearType.MANUAL

    def _build_model(self):
        self._car._model = "G4"

    def _build_company(self):
        self._car._company = "Toyota"

    def _build_year(self):
        self._car._year = 2015

