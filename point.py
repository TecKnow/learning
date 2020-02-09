class Point:
    def __init__(self, x, y, z):
        self.x, self.y, self.z = x, y, z

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, other):
        return Point(self.x * other, self.y * other, self.z * other)

    __rmul__ = __mul__

    def __eq__(self, other):
        return (self.x, self.y, self.z) == (other.x, other.y, other.z)

    def __iter__(self):
        return iter((self.x, self.y, self.z))

    def __repr__(self):
        return f"Point(x={self.x}, y={self.y}, z={self.z})"
