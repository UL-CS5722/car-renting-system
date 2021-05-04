import unittest
from ..utils import GearType
from ..vehicles import Director, HyundaiBuilder


class TestVehicleBuilder(unittest.TestCase):

    def test_create_hyundai_car(self):
        # arrange
        hyundai_builder = Director(HyundaiBuilder())

        # act
        hyundai_builder.build_car()
        hyundai = hyundai_builder.get_car()

        # assert
        self.assertEqual(hyundai._seats, 5)
        self.assertEqual(hyundai._gear_type, GearType.MANUAL)
        self.assertEqual(hyundai._model, "UltraSpec")
        self.assertEqual(hyundai._company, "Hyundai")
        self.assertEqual(hyundai._year, 2020)

