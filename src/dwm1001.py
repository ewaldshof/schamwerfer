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
            line = self.serial.readline().decode("utf-8")
            if line == "": # EOF
                return False
            line = self.no_prompt.sub("", line.strip()).split(",")
            if len(line) >= 8:
                type, id = line[0], line[2]
                x, y, z = float(line[3]), float(line[4]), float(line[5])
                callback(self, id, x, y, z)

    def send(self, string=""):
        self.serial.write((string + "\r\n").encode("utf-8"))

# Example: Read from ttyS5 and print positions to console.
if __name__ == "__main__":
    def printer(dwm, id, x, y, z):
        print(id, x, y, z)
    DWM1001("/dev/ttyS5").listen(printer)
