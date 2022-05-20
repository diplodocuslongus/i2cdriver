# https://electricdollarstore.com/led.html
import sys
import time

from i2cdriver import I2CDriver, EDS

if __name__ == '__main__':
    i2 = I2CDriver(sys.argv[1])

    d = EDS.LED(i2)
    TEAL    = 0x008080
    ORANGE  = 0xffa500
    try:
        while 1:
            time.sleep(1)
            d.hex(TEAL, 3)
            time.sleep(1)
            d.hex(ORANGE, 3)
    except:
        print('keyboard interrupt turning off')
        d.hex(0x000000, 0)
