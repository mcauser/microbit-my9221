from microbit import *
from my9221 import MY9221

ledbar = MY9221(di=pin1, dcki=pin2, reverse=False)

while True:
    for i in range(1024):
        ledbar.bits(i)
