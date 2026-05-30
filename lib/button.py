import digitalio
import board

class Button:
    def __init__(self, pin, pullDown=True):
        # Create DigitalInOut object
        self.pin = digitalio.DigitalInOut(pin)
        self.pin.direction = digitalio.Direction.INPUT

        # CircuitPython uses Pull.UP or Pull.DOWN
        if pullDown:
            self.pin.pull = digitalio.Pull.DOWN
        else:
            self.pin.pull = digitalio.Pull.UP

        self.pd = pullDown

    def is_pressed(self):
        if self.pd:
            return self.pin.value == True
        else:
            return self.pin.value == False

    def pressed(self):
        return self.is_pressed()