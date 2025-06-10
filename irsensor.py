import lgpio
import time
from w1thermsensor import W1ThermSensor, Sensor, Unit
from w1thermsensor.errors import SensorNotReadyError, NoSensorFoundError


def get_state2():
    # Open GPIO chip
    h = lgpio.gpiochip_open(0)

    ledPin = 5  # BCM 5 = physical pin 29

    # Set GPIO as output
    lgpio.gpio_claim_output(h, ledPin)

    try:
        if heat_on:
            lgpio.gpio_write(h, ledPin, 1)  # HIGH
        else:
            lgpio.gpio_write(h, ledPin, 0)  # LOW
    except KeyboardInterrupt:
        print("Heating interrupted.")
        lgpio.gpio_write(h, ledPin, 0)  
    finally:
        lgpio.gpiochip_close(h)


def get_state():
    
    sensor = InputDevice(17)
    
    while True:
        if sensor.is_active:
            print("No obstacle detected")
        else:
            print("Obstacle detected")
        time.sleep(0.5)

def get_stateh():
    # Constants
    GPIO_CHIP = 0         # Default chip index
    GPIO_PIN = 17         # BCM GPIO number
    POLL_INTERVAL = 0.5   # Seconds

    # Open a handle to the GPIO chip
    h = lgpio.gpiochip_open(GPIO_CHIP)

    # Configure the pin as input
    lgpio.gpio_claim_input(h, GPIO_PIN)

    try:
        while True:
            level = lgpio.gpio_read(h, GPIO_PIN)
            if level == 1:
                print("No obstacle detected")  # Sensor not triggered
            else:
                print("Obstacle detected")     # Sensor triggered
            time.sleep(POLL_INTERVAL)

    except KeyboardInterrupt:
        print("Stopped by user.")

    finally:
        lgpio.gpiochip_close(h)



def get_state3():
    # Constants
    GPIO_CHIP = 0         # Default chip index
    GPIO_PIN = 17         # BCM GPIO number
    POLL_INTERVAL = 0.5   # Seconds

    # Open a handle to the GPIO chip
    h = lgpio.gpiochip_open(GPIO_CHIP)

    # Configure the pin as input
    lgpio.gpio_claim_input(h, GPIO_PIN)

    try:
        level = lgpio.gpio_read(h, GPIO_PIN)
        if level == 1:
            print("No obstacle detected")  # Sensor not triggered
        else:
            print("Obstacle detected")     # Sensor triggered
        return level

    except KeyboardInterrupt:
        print("Stopped by user.")

    finally:
        lgpio.gpiochip_close(h)
