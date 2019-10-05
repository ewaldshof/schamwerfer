# Schamwerfer

## The Schamwerfer is intended for to enable technology assisted consentual adult BDSM play. Use extreme caution when playing with electricity and only do so if you have the appropriate experience to do so safely. Also, note there are inherent dangers in BDSM play especially when using electicity. Risk aware kink is the rule here.  If you don't actually know what you're doing find someone who does before hacking/playing. 

### Purpose:
1. A light that follows a person wearing a radio beacon within a defined area automatically.
2. A electroshock device which shocks the individual wearing the radio beacon according to software defined rules.
3. Manual triggering of electroshocks based on software defined rules.

### Current Development Status:
* Tens device works.
* Housing not yet complete.
* Light and beacon are both working and the light is able to track a beacon with half a meter. The accuracy could be increased by using more beacons.
* Integration between the light and the electroshock device is not complete and is a topic for future work.

### General Tools needed: 
* Mac / PC / Linux computer
* [Laser rangefinder or meter tape any model will do](images/Laser_Rangefinder.JPG)

### Beacon and Lighting Hardware:
* [decaWave MDEK1001 Module Development & Evaluation Kit](https://www.decawave.com/product/mdek1001-deployment-kit/)

### Tens Device
Tens is a German word for medical devices intended to deliver a theraputic level of electrical current to a person for the purposes of physical therapy for instance. Here we're using the tens device for BDSM. 

This tens device outputs 0-90 Volts (adjustable), 70 Milliamps, DC and does so in a pulse of .2 milseconds.
The pulse length is very short which makes the device relatively safe for individuals without any heart problems or similar conditions. Generally medical tens devices are safe to hack with as long as you leave the circuitry as is since they are intended for human. In order to determine the voltage output we used a osilosope to test the device output.

On the device itself:
1. You can use the frequency knob to set a frequency of 0-100 Hz. Practically this means that number of impulses per minute felt by the willing victim increases as the number of Hz goes up.
2. You can use the intensity know to set the voltage output from 0-90 v with a fixed 70 milliamps DC in a set pulse of .2 miliseconds. A higher voltage will hurt more.

 The tens device build out has its own readme which in particular describes the MQTT messaging settings which allow you to connect a smartphone to control the shocks.  The tens device must be in connected to the MQTT server used via wifi (provided by the microcontroller) any MQTT client can be used to control it. The tens readme can be found [here](Tens/tens_readme.md).

1. Development Breadboard

2. [2 Relay Module (SRD-05VDC-SL-C)](images/Relay_close_up.JPG)
The Relay Module can be bought [here](https://www.amazon.de/Ecloud-Relais-Module-Arduino-Special/dp/B00AE1P8KM/ref=asc_df_B00AE1P8KM/?tag=googshopde-21&linkCode=df0&hvadid=309008177512&hvpos=1o1&hvnetw=g&hvrand=5231740458383803378&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9044434&hvtargid=pla-709473331191&psc=1&th=1&psc=1&tag=&ref=&adgrpid=65257070361&hvpone=&hvptwo=&hvadid=309008177512&hvpos=1o1&hvnetw=g&hvrand=5231740458383803378&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9044434&hvtargid=pla-709473331191)
3. Connectors and wires for prototyping and breadboarding
4. [Pierenkemper GmbH Tens Device](images/Pierenkemper_housing.JPG)
5. [Microcontroller ESP32 Developer Board](images/Microcontroller_close_up.jpg)
This could be swapped out against any microcontroller with micro-python ability. It has wifi, Bluetooth LE, and Lora which we don't use in this project.
The exact board can be found [here](https://heltec.org/project/wifi-lora-32/)

Software Dependencies: 
* Python 3.7
* Micropython 1.1

Software Tools: 
1. IDE [VSCode](https://code.visualstudio.com) or similar
2. [MQTT Box](http://workswithweb.com/mqttbox.html)
Any MQTT client can be used. We used MQTT Box and also tested using an Android based MQTT client.
Screenshots for server setup can be found [here](images/MQTT_Box_Setup.png) and the setup for the commands can be found [here](images/MQTT_Interaction_Setup.png)

