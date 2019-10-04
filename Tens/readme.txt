# Flash Firmware
esptool.py --chip esp32 --port COM19 --baud 115200 write_flash -z 0x1000 esp32-20191003-v1.11-387-ga069340c1.bin

# Upload Files
ampy --port COM19 put main.py

#REPL starten - Microcontroller-Console
rshell --port COM19 repl

# MQTT
Topic: tens/value
Payload: {"Power":true,"PulseOn":150,"PulseOff":100, "Count":5}

