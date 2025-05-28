import time
import RPi.GPIO as GPIO
#from w1thermsensor import W1ThermSensor, Sensor, Unit
#from w1thermsensor.errors import SensorNotReadyError
#from w1thermsensor import W1ThermSensor, Unit, SensorNotReadyError, NoSensorFoundError



#def get_temperature():
#    try:
#        sensor = W1ThermSensor()
#        temp = sensor.get_temperature(Unit.DEGREES_C)
#        return temp
#    except NoSensorFoundError:
#        print("No sensor found. Check wiring and /boot/firmware/config.txt.")
#    except SensorNotReadyError:
#        print("Sensor is not ready. Try again shortly.")


def set_heat(heat_on):
    GPIO.setwarnings(False)
    ledPin = 5    

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(ledPin, GPIO.OUT)

    while True:
        GPIO.output(ledPin, GPIO.HIGH)
        time.sleep(5)
        GPIO.output(ledPin, GPIO.LOW)
        time.sleep(2)

#    GPIO.cleanup();


def set_cool(cool_on):
    GPIO.setwarnings(False)
    ledPin = 26    

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(ledPin, GPIO.OUT)

    try:
        while True:
            GPIO.output(ledPin, GPIO.HIGH)
            time.sleep(2)
            GPIO.output(ledPin, GPIO.LOW)
            time.sleep(2)
    except KeyboardInterrupt:
        print("Cooling interrupted.")
    finally:
        GPIO.cleanup()


def set_alarm(alarm_state):
    GPIO.setwarnings(False)
    ledPin = 13

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(ledPin, GPIO.OUT)

    try:
        while True:
            GPIO.output(ledPin, GPIO.HIGH)
            time.sleep(5)
    except KeyboardInterrupt:
        print("Alarm interrupted.")
    finally:
        GPIO.cleanup()
