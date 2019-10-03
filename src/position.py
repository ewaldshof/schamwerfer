class Position:

    def __init__(self, x, y, z):
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)

    def __str__(self):
        return "({0:.2f}, {1:.2f}, {2:.2f})".format(self.x, self.y, self.z)

    def tilt_pan_to(self, target):
        """Return tilt and pan angles for pointing at the position "target".

        Tilt is in degrees, 0 equals the Z axis ("up"), 180 along X axis,
        -180 along X axis in the negative direction.

        Pan is in degrees, 0 along X axis, 90 along Y axis in the negative
        direction, 180 along X (negative), 270 along Y (positive)."""
        # TODO: To be implemented.
