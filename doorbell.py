import RPi.GPIO as GPIO

buzzeRPin = 11
buttonPin = 12

def setup():
    print('Program is starting...')
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(buzzeRPin, GPIO.OUT)
    GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def loop():
    while True:
        if GPIO.input(buttonPin) == GPIO.LOW:
            GPIO.output(buzzeRPin, GPIO.HIGH)
            print('Buzzer on')
        else:
            GPIO.output(buzzeRPin, GPIO.LOW)
            print('Buzzer off')

def destroy():
    GPIO.output(buzzeRPin, GPIO.LOW)
    GPIO.cleanup()

if __name__ == '__main__':
    setup()
    try:
        loop()
    except KeyboardInterrupt:
        destroy()


