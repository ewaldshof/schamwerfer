from machine import Pin, Timer
import time
from task import Task

class state(object):
    def __init__(self, PinNummer):
        self.myPin=Pin(PinNummer,Pin.OUT)
        self.reset()
        self.powerWert=1
        self.pulseWert = 5000
        self.tim = Timer(-1)
        self.period = -1
        self.tim.init(period = self.period, mode=Timer.PERIODIC, callback=lambda t:print("Hallo Christoph"))
 
    def reset(self):
        self.myPin.off()
    
    def setPower(self, Wert):
        self.powerWert = not Wert
        self.myPin.value(self.powerWert)

    def getPower(self):
        return self.myPin.value()

    def SetPulseInterval(self,interval):
        self.PulseWert = interval
        self.myPin.value(interval)

class Pulse(Task):
    def __init__(self, myPulse):
        super().__init__()
        self.on_time = 100
        self.off_time = 300
        self.pulse_count = 5
        self.pulsing = False
        self.on = False
        self.countdown = self.interval = 0
        self.pulse = myPulse

    def update(self, scheduler):
        if self.pulsing:
            if self.on:
                self.interval = self.off_time
                self.pulse_count -= 1
                if self.pulse_count <= 0:
                    self.pulsing = False
            else:
                self.interval = self.on_time
            self.on = not self.on
            self.pulse.setPower(self.on)
            self.countdown = self.interval

    def initiatePulse(self, pulseOn=1000, pulseOff = 1000, count=5):
        self.on_time = pulseOn
        self.off_time = pulseOff
        self.pulse_count = count
        self.pulsing = True
