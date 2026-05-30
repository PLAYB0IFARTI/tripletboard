# general use imports
from time import sleep
import digitalio
import board
import analogio
import usb_hid
# oled display
import adafruit_displayio_sh1106
from adafruit_display_text import label
# keyboard functions
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
# custom classes
from joystick import Joystick
from button import Button

# constants
# for gpio pins, USE board.GP{pin number}, eg board.GP5
WIDTH = 128
HEIGHT = 64
SDA = board.GP2
SCL = board.GP3
ADDR = 0x3C

# oled stuff
displayio.release_displays()
i2c = busio.I2C(SDA,SCL)
display_bus = displayio.I2CDisplay(i2c, device_address=ADDR)
display = adafruit_displayio_sh1106.SH1106(display_bus, width=WIDTH, height=HEIGHT)

# making text (splash is like screen to be uploaded)
splash = displayio.Group()
text = label.Label(terminalio.FONT, text="Hello SH1106!", color=0xFFFFFF, x=10, y=20)
splash.append(text)
# actually pushes it to the screen
display.root_group = splash

# pins for the joystick
X_pin = analogio.AnalogIn(board.GP27)
Y_pin = analogio.AnalogIn(board.GP26)

# declaring sum stuff
BUTTON_1 = Button(board.GP18)
BUTTON_2 = Button(board.GP19)
BUTTON_3 = Button(board.GP20)
BUTTON_4 = Button(board.GP22) 
Sticks = Joystick(X_pin, Y_pin)



while True:
    try:
        print(Sticks.get_x())
        print(Sticks.get_y())
        if BUTTON_1.pressed():
            print("Hi")
        if BUTTON_2.pressed():
            print("b2")
        if BUTTON_3.pressed():
            print("b3")
        sleep(1)
    except:
        pass