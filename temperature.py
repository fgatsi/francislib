import lgpio
import time
from w1thermsensor import W1ThermSensor, Sensor, Unit
from w1thermsensor.errors import SensorNotReadyError, NoSensorFoundError


# Open GPIO chip
#h = lgpio.gpiochip_open(0)

def get_temperature():
    try:
        sensor = W1ThermSensor()
        temp = sensor.get_temperature(Unit.DEGREES_C)
        return temp
    except NoSensorFoundError:
        print("No sensor found. Check wiring and /boot/firmware/config.txt.")
    except SensorNotReadyError:
        print("Sensor is not ready. Try again shortly.")


def set_heat(heat_on):
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


def set_cool(cool_on):
    # Open GPIO chip
    h = lgpio.gpiochip_open(0)

    ledPin = 26  # BCM 26 = physical pin 37

    # Set GPIO as output
    lgpio.gpio_claim_output(h, ledPin)

    try:
        if cool_on:
            lgpio.gpio_write(h, ledPin, 1)  # HIGH
        else:
            lgpio.gpio_write(h, ledPin, 0)  # LOW
    except KeyboardInterrupt:
        print("Cooling interrupted.")
        lgpio.gpio_write(h, ledPin, 0)
    finally:
        lgpio.gpiochip_close(h)

