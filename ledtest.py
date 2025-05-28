import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)

ledPin = 11
GPIO.setmode(GPIO.BOARD)
GPIO.setup(ledPin, GPIO.OUT)
#GPIO.output(ledPin, GPIO.LOW)

while True:
    GPIO.output(ledPin, GPIO.HIGH)
    time.sleep(5)
    GPIO.output(ledPin, GPIO.LOW)
    time.sleep(2)

GPIO.cleanup();
