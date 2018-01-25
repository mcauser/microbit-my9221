from microbit import *
from my9221 import MY9221

ledbar = MY9221(di=pin1, dcki=pin2, reverse=False)

# Example using 8bit greyscale mode (default)
# LED brightness 0x00-0xFF

ledbar._write16(0x00) # command
ledbar._write16(0xFF) # led 1
ledbar._write16(0xFF) # led 2
ledbar._write16(0x00) # led 3
ledbar._write16(0x00) # led 4
ledbar._write16(0x00) # led 5
ledbar._write16(0xFF) # led 6
ledbar._write16(0xFF) # led 7
ledbar._write16(0x00) # led 8
ledbar._write16(0x00) # led 9
ledbar._write16(0x00) # led 10
ledbar._write16(0x00) # unused channel, required
ledbar._write16(0x00) # unused channel, required
ledbar._latch()

# Example using 12bit greyscale mode
# LED brightness 0x000-0xFFF

ledbar._write16(0x0100) # command
ledbar._write16(0x0FFF) # led 1
ledbar._write16(0x0000) # led 2
ledbar._write16(0x00FF) # led 3
ledbar._write16(0x0000) # led 4
ledbar._write16(0x000F) # led 5
ledbar._write16(0x000F) # led 6
ledbar._write16(0x0000) # led 7
ledbar._write16(0x00FF) # led 8
ledbar._write16(0x0000) # led 9
ledbar._write16(0x0FFF) # led 10
ledbar._write16(0x0000) # unused channel, required
ledbar._write16(0x0000) # unused channel, required
ledbar._latch()

# Example using 14bit greyscale mode
# LED brightness 0x000-0x3FFF

ledbar._write16(0x0200) # command
ledbar._write16(0x3FFF) # led 1
ledbar._write16(0x03FF) # led 2
ledbar._write16(0x0000) # led 3
ledbar._write16(0x0000) # led 4
ledbar._write16(0x0000) # led 5
ledbar._write16(0x003F) # led 6
ledbar._write16(0x0003) # led 7
ledbar._write16(0x0000) # led 8
ledbar._write16(0x0000) # led 9
ledbar._write16(0x0000) # led 10
ledbar._write16(0x0000) # unused channel, required
ledbar._write16(0x0000) # unused channel, required
ledbar._latch()

# Example using 16bit greyscale mode
# LED brightness 0x0000-0xFFFF

ledbar._write16(0x0300) # command
ledbar._write16(0xFFFF) # led 1
ledbar._write16(0x0FFF) # led 2
ledbar._write16(0x00FF) # led 3
ledbar._write16(0x000F) # led 4
ledbar._write16(0x0007) # led 5
ledbar._write16(0x0003) # led 6
ledbar._write16(0x0001) # led 7
ledbar._write16(0x0000) # led 8
ledbar._write16(0x0000) # led 9
ledbar._write16(0x0000) # led 10
ledbar._write16(0x0000) # unused channel, required
ledbar._write16(0x0000) # unused channel, required
ledbar._latch()
