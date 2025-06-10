import lgpio
import time


def set_alarm(alarm_state):
    ledPin = 13  # BCM 13 = physical pin 33

    # Open the GPIO chip (chip 0 is the default on Pi)
    h = lgpio.gpiochip_open(0)

    # Set the pin as output
    lgpio.gpio_claim_output(h, ledPin)

    try:
        if alarm_state:
            lgpio.gpio_write(h, ledPin, 1)  # HIGH
            #time.sleep(5)
            #lgpio.gpio_write(h, ledPin, 0)
        else:
            lgpio.gpio_write(h, ledPin, 0)  # LOW
    except KeyboardInterrupt:
        print("Alarm interrupted.")
        lgpio.gpio_write(h, ledPin, 0)
    finally:
        # Release the GPIO chip
        lgpio.gpiochip_close(h)
