import RPi.GPIO as GPIO
import smbus
import time

address = 0x48
bus = smbus.SMBus(1)
cmd = 0x40
Z_pin = 12

def analogRead(chn):
    bus.write_byte(address,cmd+chn)
    value = bus.read_byte(address)
    value = bus.read_byte(address)
    return value

def analogWrite(value):
    bus.write_byte_data(address,cmd,value)

def setup():
    global p_Red,p_Green,p_Blue
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(Z_pin,GPIO.IN,GPIO.PUD_UP)

def loop():
    while True:
        val_Z = GPIO.input(Z_pin)
        val_Y = analogRead(0) # THERES WAS INCORRECT, this is channel 0 not 1
        val_X = analogRead(1) # THERES WAS INCORRECT, this is channel 1 not 2
        print('value X: {}, \tvalue Y: {}, \tvalue Z: {}'.format(val_X,val_Y,val_Z))
        time.sleep(.01)

def destroy():
    bus.close()
    GPIO.cleanup()

if __name__=="__main__":
    print('Program starting...')
    setup()
    try:
        loop()
    except KeyboardInterrupt:
        destroy()
