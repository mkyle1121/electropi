import RPi.GPIO as GPIO
import smbus
import time

address = 0x48
bus = smbus.SMBus(1)
cmd = 0x40
ledPin = 11

def analogRead(chn):
    value = bus.read_byte_data(address,cmd+chn)
    return value

def analogWrite(value):
    bus.write_byte_data(address,cmd,value)

def setup():
    global p
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(ledPin, GPIO.OUT)
    GPIO.output(ledPin, GPIO.LOW)

    p = GPIO.PWM(ledPin, 1000)
    p.start(0)

def loop():
    while True:
        value = analogRead(0)
        p.ChangeDutyCycle(value*100/255)
        voltage = value / 255.0 * 3.3
        print('ADC value : {}, Voltage : {}'.format(value,voltage))
        time.sleep(.01)

def destroy():
    bus.close()
    GPIO.cleanup()

if __name__=='__main__':
    print('Program starting...')
    setup()
    try:
        loop()
    except KeyboardInterrupt:
        destroy()
