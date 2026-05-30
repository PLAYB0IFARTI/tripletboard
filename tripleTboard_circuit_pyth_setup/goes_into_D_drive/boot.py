import usb_hid
from hid_gamepad import gamepad_device

usb_hid.enable((usb_hid.Device.KEYBOARD, gamepad_device))