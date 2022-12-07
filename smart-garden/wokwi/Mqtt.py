from umqtt.simple import MQTTClient
import time

class Mqtt():
    SERVER = "industrial.api.ubidots.com"
    PORT = 1883
    USER = "BBFF-PnWgejj7elVnQbQUGcBT0CM6nINcOd"
    PASSWORD = ""
    ID = "1020"

    client = MQTTClient

    def __init__(self, callback):
        self.client = MQTTClient(self.ID, self.SERVER, self.PORT, self.USER, self.PASSWORD, keepalive=60)
        self.client.set_callback(callback)
        self.client.connect()

    def publish(self, channel, message):
        print(channel[25:], '📡 📡 📡 ', message)
        self.client.publish(channel, message)

    def subscribe(self, channel):
        self.client.subscribe(channel)

    def _check_msg(self):
        self.client.check_msg()
