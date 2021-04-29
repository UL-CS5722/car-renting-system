from enum import Enum
import logging

class GearType(Enum):
    AUTOMATIC = 1
    MANUAL = 2

class StatusState(Enum):
    FREE = 0
    BOOKED = 1
    CHECKOUT = 2
    RETURNED = 3

#define a logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("ola_rent")
