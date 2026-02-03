from points import Point

class Triangle:
	"""Klasa reprezentująca trójkąt na płaszczyźnie."""

	def __init__(self, x1, y1, x2, y2, x3, y3):
		self.pt1 = Point(x1, y1)
		self.pt2 = Point(x2, y2)
		self.pt3 = Point(x3, y3)

	# "[(x1, y1), (x2, y2), (x3, y3)]"
	def __str__(self):
		return f"[{self.pt1}, {self.pt2}, {self.pt3}]"

	# "Triangle(x1, y1, x2, y2, x3, y3)"
	def __repr__(self):
		return (f"Triangle({self.pt1.x}, {self.pt1.y}, {self.pt2.x}, {self.pt2.y}, "
				f"{self.pt3.x}, {self.pt3.y})")

	# obsługa tr1 == tr2
	def __eq__(self, other):
		if isinstance(other, Triangle):
			return {self.pt1, self.pt2, self.pt3} == {other.pt1, other.pt2, other.pt3}

		return NotImplemented

	# obsługa tr1 != tr2
	def __ne__(self, other):
		return not self == other

	# zwraca środek (masy) trójkąta
	def center(self):
		x1, y1 = self.pt1.x, self.pt1.y
		x2, y2 = self.pt2.x, self.pt2.y
		x3, y3 = self.pt3.x, self.pt3.y

		return Point(round((x1 + x2 + x3) / 3, 3), round((y1 + y2 + y3) / 3, 3    ))

	# pole powierzchni
	def area(self):
		x1, y1 = self.pt1.x, self.pt1.y
		x2, y2 = self.pt2.x, self.pt2.y
		x3, y3 = self.pt3.x, self.pt3.y

		return 0.5 * abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2))

	# przesunięcie o (x, y)
	def move(self, x, y):
		return Triangle(self.pt1.x + x, self.pt1.y + y,
						self.pt2.x + x, self.pt2.y + y,
						self.pt3.x + x, self.pt3.y + y)
