import lgpio
import time

# Open GPIO chip
h = lgpio.gpiochip_open(0)

def set_heat(heat_on):
    ledPin = 5  # BCM 5 = physical pin 29

    # Set GPIO as output
    lgpio.gpio_claim_output(h, ledPin)

    try:
        while True:
            lgpio.gpio_write(h, ledPin, 1)  # HIGH
            time.sleep(5)
            lgpio.gpio_write(h, ledPin, 0)  # LOW
            time.sleep(2)
    except KeyboardInterrupt:
        print("Heating interrupted.")
        lgpio.gpio_write(h, ledPin, 0)
    finally:
        lgpio.gpiochip_close(h)


def set_cool(cool_on):
    ledPin = 26  # BCM 26 = physical pin 37

    # Set GPIO as output
    lgpio.gpio_claim_output(h, ledPin)

    try:
        while True:
            lgpio.gpio_write(h, ledPin, 1)  # HIGH
            time.sleep(2)
            lgpio.gpio_write(h, ledPin, 0)  # LOW
            time.sleep(2)
    except KeyboardInterrupt:
        print("Cooling interrupted.")
        lgpio.gpio_write(h, ledPin, 0)
    finally:
        lgpio.gpiochip_close(h)


def set_alarm(alarm_state):
    ledPin = 13  # BCM 13 = physical pin 33

    # Open the GPIO chip (chip 0 is the default on Pi)
    h = lgpio.gpiochip_open(0)

    # Set the pin as output
    lgpio.gpio_claim_output(h, ledPin)

    try:
        while True:
            lgpio.gpio_write(h, ledPin, 1)  # HIGH
            time.sleep(5)
    except KeyboardInterrupt:
        print("Alarm interrupted.")
        lgpio.gpio_write(h, ledPin, 0)
    finally:
        # Release the GPIO chip
        lgpio.gpiochip_close(h)
