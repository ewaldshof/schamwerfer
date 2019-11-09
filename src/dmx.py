"""lixda dmx channels
1 - pan
2 - pan16
3 - tilt
4 - tilt16
5 - spped
6 - master dimming
7 - strobe
8 - red
9 - green
10 - blue
11 - white
"""

import pyudmx.pyudmx as pyudmx
from time import sleep
import math


class MiniBeam:
    # data array indexes
    PAN = 0
    PAN16 = 1
    TILT = 2
    TILT16 = 3
    SPEED = 4
    DIM = 5
    STROBE = 6
    RED = 7
    GREEN = 8
    BLUE = 9
    WHITE = 10

    # calibrateion
    TILT90M = 31*256  # this value points horizontically towards display (pan = 0)
    TILT90P = 224*256 # this value points horizontically towards connectors (pan = 0)
    PANFRONT = 86*256 # this tilt value points towards display (tilt= TILT90P)
    PANBACK  = 0 # this tilt value points towards connectors (tilt = TILT90P)

    # channel = first dmx channel of the beam
    # x,y,z, pan, tilt = orientation of the beam in room coordinats
    # tilt = 0 points upwards
    # pan = 0 points towards y axis
    def __init__(self, channel, x=0, y=0, z=0, pan=0, tilt=0):
        assert 0 <= channel < 245
        self.x = x
        self.y = y
        self.z = z
        self.pan = pan
        self.tilt = tilt
        self.dev = pyudmx.uDMXDevice()
        self.channel = channel
        self.data = [0]*11
        self.open()

        # pan in degrees point upwards
        # positive values pan towards connectors if tilt==0
        self.tilt_full_circle = 2.0 * (self.TILT90P - self.TILT90M)
        self.tilt0 = self.TILT90M + self.tilt_full_circle/4
        self.pan_full_circle = 2 * (self.PANFRONT - self.PANBACK)
        self.pan0 = self.PANFRONT

    # assume that there is only one DMX interface in system
    def open(self):
        self.dev.open()
        self.setRGBWDS(0,0,0,0,0,0)
        self.setDirRaw(128*256, 128*256)
        self.update()

    def close(self):
        self.dev.close()

    def update(self):
        try:
            self.dev.send_multi_value(self.channel, self.data)
        except:
            print("libusb KARPOTT")

    def setRGBWDS(self, red, green, blue, white=0, dim=255, strobe=0):
        assert 0 <= red   < 256
        assert 0 <= green < 256
        assert 0 <= blue  < 256
        assert 0 <= white < 256
        assert 0 <= dim   < 256
        self.data[self.RED]     = red
        self.data[self.GREEN]   = green
        self.data[self.BLUE]    = blue
        self.data[self.WHITE]   = white
        self.data[self.DIM]     = dim
        self.data[self.STROBE]  = strobe

    #tilt: 196 steps are 196 degrees
    # 98+28 = 126 ist senkrecht

    def pan360toRaw(self, pan):
        return self.pan0 - pan*self.pan_full_circle/360

    def tilt360toRaw(self, tilt):
        return self.tilt0 + tilt*self.tilt_full_circle/360

    # aim the beam at a point in space
    # relative to the coordinate system of the beam:
    # z axis upwards
    # y axis from back towards display
    # x axis from power connector towards dmx connector

    # could be a class method
    def computePanTiltFromPoint360(self, x, y, z):
        hxy = math.hypot(x,y)
        pan = 180.0 * math.atan2(x, y) / math.pi  # x, y flipped on purpose for rotation
        tilt = 90.0 - 180.0 * math.atan2(z, hxy) / math.pi
        return pan, tilt

    #could be a class method
    def normalizePanTilt360(self, pan, tilt):
        npan = ((pan+180.0)%360.0)-180
        ntilt = ((tilt+180.0)%360.0)-180
        return npan, ntilt

    def pointAt(self, x, y, z):
        pan, tilt = self.computePanTiltFromPoint360(x -self.x, y-self.y, z-self.y)
        npan, ntilt = self.normalizePanTilt360(pan-self.pan, tilt-self.tilt)
        self.setDir360(npan, ntilt)

    # same as above but ignores beam position and orientation
    def pointAtRel(self, x, y, z):
        pan, tilt = self.computePanTiltFromPoint360(x, y, z)
        #print("({0},{1},{2}) -> ({3}, {4})".format(x,y,z,pan,tilt))
        self.setDir360(pan, tilt)

    # coordinate system for 360° pan and tilt:
    # pan axis 0° point towards display
    # positive angles towards dmx connectors
    # negative angles towards power connector
    # tilt axis 0° points upwards
    # if pan=0 positive angles tilt towards display

    def setDir360(self, pan, tilt, speed=0):
        assert -180.0 <= tilt <= +180.0
        assert -180.0 <= pan  <= +180.0
        pan_i = self.pan360toRaw(pan)
        tilt_i = self.tilt360toRaw(tilt)
        self.setDirRaw(int(pan_i), int(tilt_i), speed)

    def setDirRaw(self, pan, tilt, speed=0):
        assert 0 <= pan  < 256*256
        assert 0 <= tilt < 256*256
        assert 0 <= speed < 256
        self.data[self.PAN]= pan >> 8
        self.data[self.TILT] = tilt >> 8

#       self.data[self.PAN16] = pan & 255
#       self.data[self.TILT16] = tilt & 0xff
        #ignore fine values for both angles
        self.data[self.PAN16] = 0
        self.data[self.TILT16] = 0
        self.data[self.SPEED] = speed


if __name__ == "__main__":
    beam = MiniBeam(1, 0.1, 0,0, 0, 0)

    sleep(2)
    beam.setRGBWDS(0, 0, 0, 255)
    #beam.setDirRaw(0,28*256)
    #beam.setDirRaw(0*256,beam.TILT90P)
    #beam.setDirRaw(2*beam.PANFRONT,beam.TILT90P)
    #beam.setDir360(-90,90)
    beam.pointAt(1,0,1)

    beam.update()
    sleep(1)
    #beam.data[beam.TILT] = 220
    beam.close()
