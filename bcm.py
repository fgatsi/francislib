import RPi.GPIO as GPIO
import time

# Set the GPIO mode (BCM or BOARD)
GPIO.setmode(GPIO.BCM)  # or GPIO.setmode(GPIO.BOARD)

# Set up GPIO pin 17 as an output
GPIO.setup(17, GPIO.OUT)

try:
    while True:
        GPIO.output(17, GPIO.HIGH)  # Turn on
        time.sleep(1)               # Wait 1 second
        GPIO.output(17, GPIO.LOW)   # Turn off
        time.sleep(1)               # Wait 1 second
except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup()  # Clean up when done

