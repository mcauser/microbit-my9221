from microbit import *
from my9221 import MY9221

ledbar = MY9221(di=pin1, dcki=pin2, reverse=False)

num = 0
ledbar.level(num)

while True:
    if button_a.was_pressed():
        num = num + 1
        ledbar.level(num)
    elif button_b.was_pressed():
        num = num - 1
        ledbar.level(num)
