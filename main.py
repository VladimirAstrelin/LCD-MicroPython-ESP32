from machine import Pin, SoftI2C
from i2c_lcd import I2cLcd
from time import sleep

I2C_ADDR = 0x27
I2C_NUM_ROWS = 4
I2C_NUM_COLS = 20

i2c = SoftI2C(sda=Pin(21), scl=Pin(22), freq=400000)
lcd = I2cLcd(i2c, I2C_ADDR, I2C_NUM_ROWS, I2C_NUM_COLS)

lcd.move_to(0, 0)
lcd.putstr("First Row")

lcd.move_to(0, 1)
lcd.putstr("Second Row")

lcd.move_to(0, 2)
lcd.putstr("Third Row")

lcd.move_to(0, 3)
lcd.putstr("Fourth Row")