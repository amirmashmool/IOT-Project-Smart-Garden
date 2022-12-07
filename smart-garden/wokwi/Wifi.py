import network
class Wifi:
    @staticmethod
    def connect():
        wlan = network.WLAN(network.STA_IF)
        wlan.active(True)
        if not wlan.isconnected():
            print('⌛⌛⌛ Connecting to WiFi')
            wlan.connect('Wokwi-GUEST', '')
            while not wlan.isconnected():
                pass
        print("🌐 👍 Connected \n")