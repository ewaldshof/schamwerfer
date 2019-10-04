from machine import Pin, Timer
import time
from task import Task

class state(object):
    def __init__(self, PinNummer):
        self.myPin=Pin(PinNummer,Pin.OUT)
        self.reset()
        self.Wert=1
        self.tim = Timer(-1)
        self.period = -1
        self.tim.init(period = self.period, mode=Timer.PERIODIC, callback=lambda t:print("Hallo Christoph"))
 
    def reset(self):
        self.myPin.off()
    
    def setPower(self, Wert):
        self.Wert = Wert
        self.myPin.value(Wert)

    def getPower(self):
        return self.myPin.value()

    def SetInterval(self,interval):
        yield

class Pulse(Task):
    def __init__(self, myPulse):
        super().__init__()
        self.rhythm = [100, 200, 100, 6000]
        self.rhythm_index = len(self.rhythm) - 1
        self.countdown = self.interval = 0
        self.pulse = myPulse
    def update(self, scheduler):
        self.rhythm_index = (self.rhythm_index + 1) % len(self.rhythm)
        self.countdown = self.interval = self.rhythm[self.rhythm_index]
        self.pulse.setPower(not self.pulse.getPower())
        #print(time.localtime())
 
