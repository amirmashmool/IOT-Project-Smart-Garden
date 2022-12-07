import dht
from machine import Pin

class Humidity:
    sensor = dht.DHT22
    def __init__(self):
        self.sensor = dht.DHT22(Pin(15))

    def temperature(self):
        self.sensor.measure()
        return self.sensor.temperature()

    def humidity(self):
        self.sensor.measure()
        return self.sensor.humidity()