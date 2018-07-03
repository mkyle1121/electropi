import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.OUT)
GPIO.output(12, GPIO.LOW)

p = GPIO.PWM(12, 50)
p.start(0)
try:
    while True:
        for i in range(0,100):
            p.ChangeDutyCycle(i)
            time.sleep(.01)
        for i in range (100,-1,-1):
            p.ChangeDutyCycle(i)
            time.sleep(.01)
except KeyboardInterrupt:
    p.stop()
    GPIO.cleanup()
