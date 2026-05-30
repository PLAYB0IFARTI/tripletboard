import usb_hid
from hid_gamepad import Gamepad
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
import time

time.sleep(2)

gp = Gamepad(usb_hid.devices)
kb = Keyboard(usb_hid.devices)

def send_button(key_name: str):
    key = getattr(Keycode, key_name.upper())
    kb.press(key)
    time.sleep(0.05)
    kb.release_all()

def send_joy_pos(xpos, ypos):
    x = int((xpos / 100) * 254 - 127)
    y = int((ypos / 100) * 254 - 127)
    x = max(-127, min(127, x))
    y = max(-127, min(127, y))
    gp.move_joysticks(x=x, y=y)


# example usage
while True:
"""
    send_joy_pos(100, 50)   # full right, center
    send_button("H")
    time.sleep(0.5)

    send_joy_pos(0, 50)     # full left, center
    send_button("E")
    time.sleep(0.5)

    send_joy_pos(50, 50)    # center
    time.sleep(0.5)
    """
