from enum import Enum
import logging

class GearType(Enum):
    AUTOMATIC = 1
    MANUAL = 2

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("ola_rent")
