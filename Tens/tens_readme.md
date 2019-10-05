This tens device outputs 0-90 Volts (adjustable), 70 Milliamps, DC and does so in a pulse of .2 milseconds.
The pulse length is very short which makes the device relatively safe for individuals without any heart problems or similar conditions. Generally medical tens devices are safe to hack with as long as you leave the circuitry as is since they are intended for human. In order to determine the voltage output we used a osilosope to test the device output.

On the device itself:
1. You can use the frequency knob to set a frequency of 0-100 Hz. Practically this means that number of impulses per minute felt by the willing victim increases as the number of Hz goes up.
2. You can use the intensity know to set the voltage output from 0-90 v with a fixed 70 milliamps DC in a set pulse of .2 miliseconds. A higher voltage will hurt more.


# Flash Firmware
esptool.py --chip esp32 --port COM19 --baud 115200 write_flash -z 0x1000 esp32-20191003-v1.11-387-ga069340c1.bin

# Upload Files
ampy --port COM19 put main.py

#REPL starten - Microcontroller-Console
rshell --port COM19 repl

# MQTT
This implimentation is specific to the hardware setup built at the sextech Hackathon in October 2019 at Ewaldshof Germany.
Duplicating the implimentation in another context would require setting up your own MQTT server or a public MQTT server and
swapping out the MQTT ServerName and Port information below.

ServerName: MQTT.ewh 
Port: 1883
Topic: tens/value
Payload: {"Power":true,"PulseOn":150,"PulseOff":100, "Count":5}

