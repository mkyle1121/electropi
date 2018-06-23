import RPi.GPIO as GPIO

ledPin = 11
buttonPin = 12
ledState = False

def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(ledPin, GPIO.OUT)
    GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def buttonEvent(channel):
    global ledState
    print('buttonEvent GPIO{}'.format(channel))
    ledState = not ledState
    if ledState:
        print('Turn on LED')
    else:
        print('Turn off LED')
    GPIO.output(ledPin, ledState) # useing boolean in place of HIGH and LOW

def loop():
    print('press button')
    GPIO.add_event_detect(buttonPin, GPIO.FALLING, callback = buttonEvent, bouncetime=300)
    # add event above, set and forget
    while True:
        pass

def destroy():
    GPIO.output(ledPin, GPIO.LOW)
    GPIO.cleanup()

if __name__ == "__main__":
    setup()
    try:
        loop()
    except KeyboardInterrupt:
        destroy()


