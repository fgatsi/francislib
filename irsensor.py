import lgpio
import time
from w1thermsensor import W1ThermSensor, Sensor, Unit
from w1thermsensor.errors import SensorNotReadyError, NoSensorFoundError


def get_state_save():
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


def get_state():
    # Constants
    GPIO_CHIP = 0         # Default chip index
    GPIO_PIN = 17         # BCM GPIO number (pin 11 in BOARD mode)
    POLL_INTERVAL = 1.0   # Seconds

    # Open a handle to the GPIO chip defined
    h = lgpio.gpiochip_open(GPIO_CHIP)

    # Configure the pin as input to read from the sensor
    lgpio.gpio_claim_input(h, GPIO_PIN)

    try:
        level = lgpio.gpio_read(h, GPIO_PIN) 
        # Note: The sensor reads '1' when there is no obstacle and '0' when one is detected
        if level == 1:
            print("No obstacle detected")  # Sensor not triggered
        else:
            print("Obstacle detected")     # Sensor triggered
        return ~level &  # Invert the level to get a HIGH when object is detetcted

    except KeyboardInterrupt:
        print("Stopped by user.")

    finally:
        lgpio.gpiochip_close(h)
