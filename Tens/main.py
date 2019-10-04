from machine import UART, Pin
import time
import statemachine
from task import Task, Scheduler
import ewh_net
from mqtt import MQTT
import ujson

# wir etablieren 2 Relaisobjekte für Pulse und Power
# Power hat 2 Stufen 1 und 0 für High und Low
# Pulse ist die Frequenz in der das Tens eingeschaltet wird.
PulsePin = 12
PowerPin = 13
myPulse = statemachine.state(PulsePin)
myPower = statemachine.state(PowerPin)
# Task für Scheduler Objekt Pulse/Power
myTask = statemachine.Pulse(myPulse)
mySchedule = Scheduler()
mySchedule.register(myTask)
# Netzwerk am Scheduler registrieren 
myNetwork = ewh_net.Network()
mySchedule.register(myNetwork)
# MQTT am Scheduler registrieren
myMqtt = MQTT(myNetwork)
mySchedule.register(myMqtt)

def on_mqtt(topic, msg):                       # Json Parser für empfangene MQTT Nachricht
    #print(topic, msg)
    data = ujson.loads(msg)
    Power = not data["Power"]
    PulseOn = data["PulseOn"]
    PulseOff = data["PulseOff"]
    Count = data["Count"]
    #print(PulseOn, PulseOff, Count, Power)
    myTask.initiatePulse(PulseOn, PulseOff, Count)
    #myPulse.SetPulseInterval(Pulse)
    myPower.setPower(Power)


myMqtt.subscribe("tens/value", on_mqtt)

print("Hello, world1!")
mySchedule.start(20)

while True:
    #myPulse.setPower(True)
    #myPower.setPower(False)
    #time.sleep(1)
    #myPulse.setPower(0)
    #myPower.setPower(1)
    #time.sleep(1)
    pass
    
    
    #pHiLo.value(1*(pHiLo.value() != 1))
    
 
