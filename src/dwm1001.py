from position import Position
import re
import serial

class DWM1001:

    def __init__(self, port):
        self.serial = serial.Serial(port=port, baudrate=115200)
        self.no_prompt = re.compile("^dwm> ")
        self.listening = False

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
            if len(line) >= 8:
                type, id = line[0], line[2]
                pos = Position(*line[3:6])
                callback(self, id, pos)

    def send(self, string=""):
        self.serial.write((string + "\r\n").encode("utf-8"))
