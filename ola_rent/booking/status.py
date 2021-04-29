from ..utils import StatusState
class Status:
    def __init__(self):
        self._state = StatusState.FREE

    def booked(self):
        self._state = StatusState.BOOKED
        return self._state

    def checkout(self):
        self._state = StatusState.CHECKOUT
        return self._state

    def retured(self):
        self._state = StatusState.RETURNED

    