from dmx import MiniBeam
from dwm1001 import DWM1001
from position import Position

class Schamwerfer:

    def __init__(self, serial_port, tag_id, beam_pos, beam_pan, beam_tilt, fixed_z=None):
        self.tag_id = tag_id
        self.fixed_z = fixed_z
        self.dwm = DWM1001(serial_port)
        self.beam = MiniBeam(1, beam_pos.x, beam_pos.y, beam_pos.z, beam_pan, beam_tilt)
        self.beam.setRGBWDS(0, 0, 0, 255)

    def update(self, dwm, id, pos):
        print(id, pos)
        if id == self.tag_id:
            self.pointAt(pos)

    def listen(self):
        self.dwm.listen(self.update)

    def pointAt(self, pos):
        self.beam.pointAt(pos.x, pos.y, self.fixed_z if self.fixed_z is not None else pos.z)
        self.beam.update()


# Example: Read from ttyS5 and locate the beam at a certain position in the room.
if __name__ == "__main__":
    Schamwerfer(
        "/dev/ttyS5",
        "0689",
        Position(6.56, 3.69, 1.08),
        0,
        0,
    ).listen()
