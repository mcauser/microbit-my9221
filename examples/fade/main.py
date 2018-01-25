from microbit import *
from my9221 import MY9221

ledbar = MY9221(di=pin1, dcki=pin2, reverse=False)

buf = bytearray([0,1,3,7,15,31,63,127,255,255])

while True:
    # Press A to fade in from left
    if button_a.is_pressed():
        ledbar.reverse(False)
        ledbar.bytes(buf)
    # Press B to fade in from right
    elif button_b.is_pressed():
        ledbar.reverse(True)
        ledbar.bytes(buf)
    sleep(100)
