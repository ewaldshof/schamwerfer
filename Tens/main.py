from machine import UART, Pin
import time
import statemachine

# wir etablieren 2 Relaisobjekte
PulsePin = 12
PowerPin = 13
myPulse=statemachine.state(PulsePin)
myPower=statemachine.state(PowerPin)

print("Hello, world1!")
while True:
    myPulse.setPower(True)
    myPower.setPower(False)
    time.sleep(1)
    myPulse.setPower(0)
    myPower.setPower(1)
    time.sleep(1)
    
    
    
    #pHiLo.value(1*(pHiLo.value() != 1))
    
 
