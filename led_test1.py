import RPi.GPIO as GPIO
import time

ledPin = 11

def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(ledPin, GPIO.OUT) # set output mode
    GPIO.output(ledPin, GPIO.LOW) # seet output to low (off)
    print('using pin {}'.format(ledPin))

def loop():
    while True:
        GPIO.output(ledPin, True)
        print ("led on")
        time.sleep(.5)
        GPIO.output(ledPin, False)
        print("led off")
        time.sleep(.5)

def destroy():
    GPIO.output(ledPin, GPIO.LOW)
    GPIO.cleanup()

if __name__ == "__main__":
    setup()
    try:
        loop()
    except KeyboardInterrupt:
        destroy()


