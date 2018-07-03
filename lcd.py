#from PCF8574 import PCF8574_GPIO
#from Adafruit_LCD1602 import Adafruit_CharLCD

from Adafruit_Python_CharLCD.Adafruit_CharLCD import Adafruit_CharLCD
import pcf8574
from time import sleep,strftime
from datetime import datetime

def get_cpu_temp():
    tmp = open('/sys/class/thermal/thermal_zone0/temp')
    cpu = tmp.read()
    tmp.close()
    return '{:.2f}'.format(float(cpu)/1000) + ' C'

def get_time_now():
    return datetime.now().strftime('    %H:%M:%S')

def loop():
    mcp.output(3,1)
    lcd.begin(16,2)
    while True:
        lcd.setCursor(0,0)
        lcd.message('CPU: ' + get_cpu_temp()+'\n')
        lcd.message(get_time_now())
        sleep(1)

def destroy():
    lcd.clear()

PCF8574_address = 0x27
PCF8574A_address = 0x3f

try:
    mcp = PCF8574_GPIO(PCF8574_address)
except:
    try:
        #mcp = PCF8574_GPIO(PCF8574A_address)
        mcp = PCF8574(1, PCF8574_address) # needed to add the serial bus number on RPi and then address
    except:
        print ("I2C Address Error!")
        exit(1)

#lcd = Adafruit_CharLCD(pin_rs=0, pin_e=2, pins_db=[4,5,6,7], GPIO=mcp)
lcd = Adafruit_CharLCD(rs=0, en=2, d4=4, d5=5, d6=6, d7=7, cols=16, lines=2)
if __name__=="__main__":
    print ('Program is starting...')
    try:
        loop()
    except KeyboardInterrupt:
        destroy()
