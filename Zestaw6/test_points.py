import unittest
from points import Point

class TestPoints(unittest.TestCase):

	def setUp(self):
		self.p1 = Point(-4, 2)
		self.p2 = Point(1, -3)
		self.p3 = Point(-4, 2)

	def test_str(self):
		cases = [
			(self.p1, "(-4, 2)"),
			(self.p2, "(1, -3)"),
			(self.p3, "(-4, 2)"),
		]

		for point, expected in cases:
			with self.subTest(point=point):
				self.assertEqual(str(point), expected, msg=f"Failure during str method test "
														   f"expected {expected} get {str(point)} instead.")

	def test_repr(self):
		cases = [
			(self.p1, "Point(-4, 2)"),
			(self.p2, "Point(1, -3)"),
			(self.p3, "Point(-4, 2)"),
		]

		for point, expected in cases:
			with self.subTest(point=point):
				self.assertEqual(repr(point), expected, msg=f"Failure during repr method test "
														   f"expected {expected} get {repr(point)} instead.")

	def test_eq(self):
		cases = [
			(self.p1, self.p2, False),
			(self.p1, self.p3, True),
			(self.p3, self.p2, False),
			(self.p3, self.p3, True),
			(self.p2, self.p2, True),
			(self.p1, self.p1, True),
		]

		for point1, point2, expected in cases:
			with self.subTest(point1=point1, point2=point2):
				self.assertEqual(point1 == point2, expected, msg=f"Failure during eq method test "
														   f"expected {expected} get {point1 == point2} instead.")

	def test_ne(self):
		cases = [
			(self.p1, self.p2, True),
			(self.p1, self.p3, False),
			(self.p3, self.p2, True),
			(self.p3, self.p3, False),
			(self.p2, self.p2, False),
			(self.p1, self.p1, False),
		]

		for point1, point2, expected in cases:
			with self.subTest(point1=point1, point2=point2):
				self.assertEqual(point1 != point2, expected, msg=f"Failure during ne method test "
														   f"expected {expected} get {point1 != point2} instead.")

	def test_add(self):
		cases = [
			(self.p1, self.p2, Point(-3, -1)),
			(self.p1, self.p3, Point(-8, 4)),
			(self.p3, self.p2, Point(-3, -1)),
			(self.p3, self.p3, Point(-8, 4)),
			(self.p2, self.p2, Point(2, -6)),
			(self.p1, self.p1, Point(-8, 4)),
		]

		for point1, point2, expected in cases:
			with self.subTest(point1=point1, point2=point2):
				self.assertEqual(point1 + point2, expected, msg=f"Failure during add method tes t"
														   f"expected {expected} get {point1 + point2} instead.")

	def test_sub(self):
		cases = [
			(self.p1, self.p2, Point(-5, 5)),
			(self.p1, self.p3, Point(0, 0)),
			(self.p3, self.p2, Point(-5, 5)),
			(self.p3, self.p3, Point(0, 0)),
			(self.p2, self.p2, Point(0, 0)),
			(self.p1, self.p1, Point(0, 0)),
		]

		for point1, point2, expected in cases:
			with self.subTest(point1=point1, point2=point2):
				self.assertEqual(point1 - point2, expected, msg=f"Failure during sub method test "
														   f"expected {expected} get {point1 - point2} instead.")

	def test_mul(self):
		cases = [
			(self.p1, self.p2, -10),
			(self.p1, self.p3, 20),
			(self.p3, self.p2, -10),
			(self.p3, self.p3, 20),
			(self.p2, self.p2, 10),
			(self.p1, self.p1, 20),
		]

		for point1, point2, expected in cases:
			with self.subTest(point1=point1, point2=point2):
				self.assertEqual(point1 * point2, expected, msg=f"Failure during mull method test"
														   f"expected {expected} get {point1 * point2} instead.")

	def test_cross(self):
		cases = [
			(self.p1, self.p2, 10),
			(self.p1, self.p3, 0),
			(self.p3, self.p2, 10),
			(self.p2, self.p1, -10),
			(self.p3, self.p1, 0),
			(self.p2, self.p3, -10),

		]

		for point1, point2, expected in cases:
			with self.subTest(point1=point1, point2=point2):
				self.assertEqual(point1.cross(point2), expected, msg=f"Failure during cross method test"
														   f"expected {expected} get {point1.cross(point2)} instead.")

	def test_lenght(self):
		cases = [
			(self.p1, 4.472135955),
			(self.p2, 3.1622776602)
		]

		for point, expected in cases:
			with self.subTest(point=point):
				self.assertAlmostEqual(point.length(), expected, places=10,
									   msg=f"Failure during lenght method test "
									   f"expected {expected} get {point.length()} instead.")

	def test_hash(self):
		self.assertEqual(hash(self.p1), hash(self.p3))
		self.assertNotEqual(hash(self.p1), hash(self.p2))

if __name__ == '__main__':
	unittest.main()