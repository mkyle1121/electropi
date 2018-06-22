import RPi.GPIO as GPIO

ledPin = 11
buttonPin = 12

def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(ledPin, GPIO.OUT)
    GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP) #button normal is UP or 3.3v

def loop():
    while True:
        if GPIO.input(buttonPin) == GPIO.LOW: # button pressed, less voltage to button GPIO 18, more to ground
            GPIO.output(ledPin, GPIO.HIGH) # turn on led
            print('led on')
        else:
            GPIO.output(ledPin, GPIO.LOW) # turn off led
            print('led off')

def destroy():
    GPIO.output(ledPin, GPIO.LOW)
    GPIO.cleanup()

if __name__ == '__main__':
    setup()
    try:
        loop()
    except KeyboardInterrupt:
        destroy()


