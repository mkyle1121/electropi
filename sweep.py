import RPi.GPIO as GPIO
import time

OFFSE_DUTY = 0.5
SERVO_MIN_DUTY = 2.5+OFFSE_DUTY
SERVO_MAX_DUTY = 12.5+OFFSE_DUTY
servoPin = 12

def map(value, fromLow, fromHigh, toLow, toHigh):
    return(toHigh - toLow)*(value - fromLow) / (fromHigh - fromLow) + toLow

def setup():
    global p
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(servoPin, GPIO.OUT)
    GPIO.output(servoPin, GPIO.LOW)

    p = GPIO.PWM(servoPin, 50)
    p.start(0)

def servoWrite(angle):
    if(angle < 0):
        angle = 0
    elif angle > 180:
        angle = 180
    p.ChangeDutyCycle(map(angle,0,180,SERVO_MIN_DUTY,SERVO_MAX_DUTY))

def loop():
    while True:
        for dc in range(0,181,1):
            servoWrite(dc)
            time.sleep(.001)
        time.sleep(.5)
        for dc in range(180,-1,-1):
            servoWrite(dc)
            time.sleep(.001)
        time.sleep(.5)

def destroy():
    p.stop()
    GPIO.cleanup()

if __name__=="__main__":
    print('Program starting')
    setup()
    try:
        loop()
    except KeyboardInterrupt:
        destroy()
