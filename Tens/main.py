from machine import UART, Pin
import time
import statemachine
from task import Task, Scheduler
import ewh_net
from mqtt import MQTT
import ujson

# wir etablieren 2 Relaisobjekte
PulsePin = 12
PowerPin = 13
myPulse = statemachine.state(PulsePin)
myPower = statemachine.state(PowerPin)
myTask = statemachine.Pulse(myPulse)
mySchedule = Scheduler()
mySchedule.register(myTask)
myNetwork = ewh_net.Network()
mySchedule.register(myNetwork)
myMqtt = MQTT(myNetwork)
mySchedule.register(myMqtt)

def on_mqtt(topic, msg):
    #print(topic, msg)
    data = ujson.loads(msg)
    print(data["Power"])
    print(data["Pulse"])


myMqtt.subscribe("tens/value", on_mqtt)

print("Hello, world1!")
mySchedule.start(100)

while True:
    #myPulse.setPower(True)
    #myPower.setPower(False)
    #time.sleep(1)
    #myPulse.setPower(0)
    #myPower.setPower(1)
    #time.sleep(1)
    pass
    
    
    #pHiLo.value(1*(pHiLo.value() != 1))
    
 
