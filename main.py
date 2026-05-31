# general use imports
import time
import digitalio
import board
import analogio
import usb_hid
# oled display

import displayio
import busio
import adafruit_displayio_sh1106
from adafruit_display_text import label
# keyboard functions

from adafruit_hid.mouse import Mouse
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
# custom classes

from joystick import Joystick
from button import Button

# constants
# for gpio pins, USE board.GP{pin number}, eg board.GP5

WIDTH = 128
HEIGHT = 64
#SDA = GP2
#SCL = GP3
# ADDR = 0x3C

# oled stuff
#displayio.release_displays()
#i2c = busio.I2C(board.GP3, board.GP2)
#display_bus = displayio.I2CDisplay(i2c, device_address=ADDR)
#display = adafruit_displayio_sh1106.SH1106(display_bus, width=WIDTH, height=HEIGHT)

# making text (splash is like screen to be uploaded)
#splash = displayio.Group()
#text = label.Label(terminalio.FONT, text="Hello SH1106!", color=0xFFFFFF, x=10, y=20)
#splash.append(text)
# actually pushes it to the screen

#display.root_group = splash

# pins for the joystick

X_pin = analogio.AnalogIn(board.GP27)
Y_pin = analogio.AnalogIn(board.GP26)

# declaring sum stuff

BUTTON_1 = Button(board.GP18)
BUTTON_2 = Button(board.GP19)
BUTTON_3 = Button(board.GP20)
BUTTON_4 = Button(board.GP22) #button press for joystick
Sticks = Joystick(X_pin, Y_pin)

# keyboard stuff
kbd = Keyboard(usb_hid.devices)

# mouse stuff
mouse = Mouse(usb_hid.devices)

print("hello world")

while True:
    try:
        #print(Sticks.get_x())
        #print(Sticks.get_y())
        #print(BUTTON_1.pin.value)
        #print(BUTTON_1.pv)
        # print(BUTTON_1.pv)
        if BUTTON_1.just_pressed():
            kbd.send(Keycode.ALT, Keycode.TAB)
            #print(BUTTON_1.pin.value)
        if BUTTON_2.pressed():
            kbd.press(Keycode.B)
        if BUTTON_3.pressed():
            kbd.press(Keycode.C)
        kbd.release_all()
        #time.sleep(1)
        
        # change in mouse pos
        
        cg_x = x=int((-(Sticks.get_x()) + 50) // -10)
        cg_y = x=int((-(Sticks.get_y()) + 50) // -10)
        
        # mouse states
        
        ms_x = cg_x != 0
        ms_y = cg_y != 0
        ms_both = ms_x or ms_y
        
        if BUTTON_4.pressed() and ms_both:
            mouse.release(Mouse.RIGHT_BUTTON)
            mouse.press(Mouse.MIDDLE_BUTTON)
        elif not BUTTON_4.pressed() and ms_both:
            mouse.release(Mouse.MIDDLE_BUTTON)
            mouse.press(Mouse.RIGHT_BUTTON)
        else:
            mouse.release(Mouse.MIDDLE_BUTTON)
            mouse.release(Mouse.RIGHT_BUTTON)
            
        mouse.move(x=cg_x, y=cg_y)
        
        # time.sleep(0.5)
    except Exception as e:
        print(e)


