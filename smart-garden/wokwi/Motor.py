from machine import Pin, PWM

class Motor:
    servo = PWM

    _value = 40

    def __init__(self):
        self.servo = PWM(Pin(13), freq=50)
        self.servo.duty(self._value)
    def open(self):
        self._value = 115
        self.servo.duty(self._value)
        print("🌊 🌊 🌊 Opened!")

    def close(self):
        self._value = 40
        self.servo.duty(self._value)
        print("🔒 🔒 🔒 Closed! \n")

    def is_open(self):
        return  self._value == 115

    def status(self):
        return "1" if self.is_open() else "0"