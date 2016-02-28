import rasp_lcd_2
from time import *

lcd = lcddriver.lcd()

lcd.lcd_display_string("Hello world", 1)
lcd.lcd_display_string("My name is", 2)