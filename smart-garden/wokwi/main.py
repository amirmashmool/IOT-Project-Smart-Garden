from machine import Pin, PWM
import time
import json

from Wifi import Wifi
from Temperature import Temperature
from Humidity import Humidity
from Light import Light
from Motor import Motor
from Mqtt import Mqtt

# Connect WiFi
Wifi.connect()

# Sensors
motor = Motor()
temperature = Temperature()
humidity = Humidity()
light = Light()

# current status
current_status = {
    "motor" : motor.status(),
    "light" : light.percentage(),
    "humidity": humidity.humidity(),
    "temperature": temperature.celsius()
}

print(current_status)


# Pars the current status to json
def toJson():

    date = {}

    date['context'] = current_status
    date['value'] = 1

    return json.dumps(date)

# MQTT Subscribe callback
def callback(channel, value):
    channel = channel.decode('ASCII')
    value = float(value.decode('ASCII'))

    if "soil" in channel:
        print("value", value)
        if value < 50 and not motor.is_open():
            motor.open()
        elif value > 50 and motor.is_open():
            motor.close()


client = Mqtt(callback)
client.subscribe("/v1.6/devices/controller/soil-moisture/lv")


while True:

    client._check_msg()

    # check if temperature is changed
    if current_status.get("temperature") != temperature.celsius():
        current_status.update({"temperature": temperature.celsius()})
        client.publish("/v1.6/devices/controller/temperature", str(temperature.celsius()))

    # check if humidity is changed
    if current_status.get("humidity") != humidity.humidity():
        current_status.update({"humidity": humidity.humidity()})
        client.publish("/v1.6/devices/controller/soil-moisture", str(humidity.humidity()))

    # check if light is changed
    if current_status.get("light") != light.percentage():
        current_status.update({"light": light.percentage()})
        client.publish("/v1.6/devices/controller/light", str(light.percentage()))

    # check if motor status is changed
    if current_status.get("motor") != motor.status():
        current_status.update({"motor": motor.status()})
        client.publish("/v1.6/devices/controller/water-controller", motor.status())

    client.publish("/v1.6/devices/controller/current-status", toJson())
    time.sleep(1)