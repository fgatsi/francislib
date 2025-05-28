import RPi.GPIO as GPIO
import time

# Set the GPIO mode
GPIO.setmode(GPIO.BCM)

# Set up GPIO pin 17
GPIO.setup(17, GPIO.OUT)

# Blink the LED
try:
    while True:
        GPIO.output(17, GPIO.HIGH)  # Turn on
        time.sleep(1)               # Wait 1 second
        GPIO.output(17, GPIO.LOW)   # Turn off
        time.sleep(1)               # Wait 1 second
except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup()                  # Clean up when done

