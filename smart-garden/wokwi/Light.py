from machine import Pin, ADC

class Light:
    sensor = ADC

    def __init__(self):
        self.sensor = ADC(Pin(35))

    def read(self):
        return self.sensor.read()

    def percentage(self):
        return 100 - float((self.read() * 100) / 4096)