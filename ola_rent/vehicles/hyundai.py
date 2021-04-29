from .abs_builder import Builder
from ..utils import GearType


class HyundaiBuilder(Builder):
    
    def _build_seats(self):
        self._car._seats = 5

    def _build_gear(self):
        self._car._gear_type = GearType.MANUAL

    def _build_model(self):
        self._car._model = "UltraSpec"

    def _build_company(self):
        self._car._company = "Hyundai"

    def _build_year(self):
        self._car._year = 2020

    # def _build_id(self):
    #     self._car._id = self._car._company + str(self._car._year)

