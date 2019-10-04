from position import Position
import re
import time
import serial

class DWM1001:

    def __init__(self, port, refresh_hz=20, min_confidence=0):
        self.serial = serial.Serial(port=port, baudrate=115200)
        self.no_prompt = re.compile("^dwm> ")
        self.listening = False
        self.min_delay = 1 / refresh_hz
        self.last_msg = None
        self.min_confidence = min_confidence

    def listen(self, callback):
        self.send()
        self.send("lep")
        self.listening = True
        while self.listening:
            line = self.serial.readline()
            if line == "": # EOF
                return False
            line = line.decode("utf-8")
            line = self.no_prompt.sub("", line.strip()).split(",")
            now = time.perf_counter()
            if len(line) >= 8 and (self.last_msg is None or (now - self.last_msg > self.min_delay)):
                type, id, confidence = line[0], line[2], int(line[6])
                pos = Position(*line[3:6])
                if confidence >= self.min_confidence:
                    self.last_msg = now
                    callback(self, id, pos)

    def send(self, string=""):
        self.serial.write((string + "\r\n").encode("utf-8"))
