import RPi.GPIO as GPIO
import time

LedPin = 12

def setup():
    global p
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(LedPin, GPIO.OUT)
    GPIO.output(LedPin, GPIO.LOW)
    p = GPIO.PWM(LedPin, 1000)
    p.start(0)

def loop():
    while True:
        for dc in range(0,100,4):
            p.ChangeDutyCycle(dc) # must be between 0 100 for duty cycle
            time.sleep(.01)
        time.sleep(1)
        for dc in range(100,-1,-4):
            p.ChangeDutyCycle(dc)
            time.sleep(.01)
        time.sleep(1)

def destroy():
    p.stop()
    GPIO.output(LedPin, GPIO.LOW)
    GPIO.cleanup()

if __name__ == "__main__":
    setup()
    try:
        loop()
    except KeyboardInterrupt:
        destroy()
