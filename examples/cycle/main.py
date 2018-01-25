from microbit import *
from my9221 import MY9221

ledbar = MY9221(di=pin1, dcki=pin2, reverse=False)

buf = [0,0,1,3,7,15,31,63,127,255]

while True:
    buf.insert(0,buf.pop())
    ledbar.bytes(buf)
    sleep(50)
