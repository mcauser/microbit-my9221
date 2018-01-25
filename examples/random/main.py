from microbit import *
import random
from my9221 import MY9221

ledbar = MY9221(di=pin1, dcki=pin2, reverse=False)

random.seed(1337)

while True:
    if button_a.was_pressed():
        ledbar.bits(random.randint(0, 1023))
