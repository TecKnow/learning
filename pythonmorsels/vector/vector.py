from dataclasses import dataclass
from numbers import Real


@dataclass(frozen=True)
class Vector:
    __slots__ = ("x", "y", "z")
    x: float
    y: float
    z: float

    def __iter__(self):
        yield from (self.x, self.y, self.z)

    def __add__(self, other):
        if not isinstance(other, self.__class__):
            raise TypeError
        x1, y1, z1 = self
        x2, y2, z2 = other
        return Vector(x1 + x2, y1 + y2, z1 + z2)

    def __sub__(self, other):
        if not isinstance(other, self.__class__):
            raise TypeError
        x1, y1, z1 = self
        x2, y2, z2 = other
        return Vector(x1 - x2, y1 - y2, z1 - z2)

    def __mul__(self, other: Real):
        if not isinstance(other, Real):
            raise TypeError
        x, y, z = self
        return Vector(x * other, y * other, z * other)

    __rmul__ = __mul__

    def __truediv__(self, other: Real):
        if not isinstance(other, Real):
            raise TypeError
        x, y, z = self
        return Vector(x / other, y / other, z / other)

    def __rtruediv__(self, other: Real):
        if not isinstance(other, Real):
            raise TypeError
        x, y, z = self
        return Vector(other / x, other / y, other / z)
