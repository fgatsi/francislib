import time
import RPi.GPIO as GPIO
from w1thermsensor import W1ThermSensor, Sensor, Unit
from w1thermsensor.errors import SensorNotReadyError


def get_temperature():
    global temp
    sensor = W1ThermSensor()
    
    while True:
        try:
            temp = sensor.get_temperature(Unit.DEGREES_C)
            print(temp)
            
        except SensorNotReadyError:
            print("Sensor is not ready. Waiting...")
        time.sleep(1)

    return temp

def set_alarm(alarm_state):
    pass



mt = get_temperature()
print(mt)
