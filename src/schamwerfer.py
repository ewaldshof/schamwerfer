from dmx import MiniBeam
from dwm1001 import DWM1001
from position import Position

class Schamwerfer:

    def __init__(self, serial_port, tag_id, beam_pos, beam_pan, beam_tilt):
        self.tag_id = tag_id
        self.dwm = DWM1001(serial_port)
        self.dmx = MiniBeam(1, beam_pos.x, beam_pos.y, beam_pos.z, beam_pan, beam_tilt)

    def update(dwm, id, pos):
        print(id, pos)
        if id == self.tag_id:
            self.dmx.pointAt(pos.x, pos.y, pos.z)

    def listen():
        self.dwm.listen(self.update)


# Example: Read from ttyS5 and print positions to console.
if __name__ == "__main__":
    Schamwerfer(
        "/dev/ttyS5",
        "0689",
        Position(6.56, 3.69, 1.08),
        0,
        0,
    )
    DWM1001("/dev/ttyS5").listen(printer)
