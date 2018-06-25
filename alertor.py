import RPi.GPIO as GPIO
import time
import math

buzzeRPin = 11
buttonPin = 12

def setup():
    global p
    print('Program is starting...')
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(buzzeRPin, GPIO.OUT)
    GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    p = GPIO.PWM(buzzeRPin, 1)
    p.start(0)

def loop():
    while True:
        if GPIO.input(buttonPin) == GPIO.LOW:
            alertor()
            print('Buzzer on')
        else:
            stopAlertor()
            print('Buzzer off')

def alertor():
    p.start(50)
    for x in range(0,361):
        sinVal = math.sin(x * (math.pi / 180.0))
        toneVal = 2000 + sinVal * 500
        p.ChangeFrequency(toneVal)
        time.sleep(.001)

def stopAlertor():
    p.stop()

def destroy():
    GPIO.output(buzzeRPin, GPIO.LOW)
    GPIO.cleanup()

if __name__ == '__main__':
    setup()
    try:
        loop()
    except KeyboardInterrupt:
        destroy()


