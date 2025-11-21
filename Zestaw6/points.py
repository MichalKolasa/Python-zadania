import math

class Point:
    """Klasa reprezentująca punkty na płaszczyźnie."""

    # Konstuktor
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Zwraca string "(x, y)"
    def __str__(self):
        return f"({self.x}, {self.y})"

    # Zwraca string "Point(x, y)"
    def __repr__(self):
        return f"Point({self.x}, {self.y})"

    # Obsługa point1 == point2
    def __eq__(self, other):
        if isinstance(other, Point):
            return self.x == other.x and self.y == other.y
        return NotImplemented

    # Obsługa point1 != point2
    def __ne__(self, other):
        return not self == other

    # Punkty jako wektory 2D.

    # v1 + v2
    def __add__(self, other):
        if isinstance(other, Point):
            return Point(self.x + other.x, self.y + other.y)
        return NotImplemented

    # v1 - v2
    def __sub__(self, other):
        if isinstance(other, Point):
            return Point(self.x - other.x, self.y - other.y)
        return NotImplemented

    # v1 * v2, iloczyn skalarny, zwraca liczbę
    def __mul__(self, other):
        if isinstance(other, Point):
            return self.x * other.x + self.y * other.y
        return NotImplemented

    # v1 x v2, iloczyn wektorowy 2D, zwraca liczbę
    def cross(self, other):
        return self.x * other.y - self.y * other.x

    # Długość wektora
    def length(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    # Bazujemy na tuple, immutable points
    def __hash__(self):
        return hash((self.x, self.y))