from machine import Pin, ADC
from math import log

class Temperature:
    sensor = ADC
    def __init__(self):
        self.sensor = ADC(Pin(34))

    def read(self):
        return self.sensor.read_u16()

    def celsius(self):
        return 1 / (log(1 / (65535 / self.read() - 1)) / 3950 + 1 / 298.15) - 273.15