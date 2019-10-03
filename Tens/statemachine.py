from machine import Pin
class state(object):
    def __init__(self, PinNummer):
        self.myPin=Pin(PinNummer,Pin.OUT)
        self.reset()
        self.Wert=1
 
    def reset(self):
        self.myPin.off()
 
    def setPower(self, Wert):
        self.Wert = Wert
        self.myPin.value(Wert)
