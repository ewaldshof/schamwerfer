from machine import UART, Pin
import time
PulsePin = 12
PowerPin = 13
pPulse=Pin(PulsePin,Pin.OUT)
pHiLo=Pin(PowerPin,Pin.OUT)


print("Hello, world1!")

while True:
    time.sleep(1)
    pHiLo.value(1*(pHiLo.value() !=1))
 
