import unittest

from Zestaw6.points import Point
from triangles import Triangle

class TestTriangle(unittest.TestCase):

	def setUp(self):
		self.t1 = Triangle(0, 0, 3, 0, 1, 2)
		self.t2 = Triangle(1, 1, 4, 2, 2, 5)
		self.t3 = Triangle(-2, 3, 0, 7, 3, 1)
		self.t4 = Triangle(0, 0, 3, 0, 1, 2) # taki jak pierwszy

	def test_str(self):
		cases = [
			(self.t1, "[(0, 0), (3, 0), (1, 2)]"),
			(self.t2, "[(1, 1), (4, 2), (2, 5)]"),
			(self.t3, "[(-2, 3), (0, 7), (3, 1)]"),
		]

		for triangle, expected in cases:
			with self.subTest(triangle=triangle):
				self.assertEqual(str(triangle), expected, msg=f"Failure during str method test "
														   f"expected {expected} get {str(triangle)} instead.")

	def test_repr(self):
		cases = [
			(self.t1, "Triangle(0, 0, 3, 0, 1, 2)"),
			(self.t2, "Triangle(1, 1, 4, 2, 2, 5)"),
			(self.t3, "Triangle(-2, 3, 0, 7, 3, 1)"),
		]

		for triangle, expected in cases:
			with self.subTest(triangle=triangle):
				self.assertEqual(repr(triangle), expected, msg=f"Failure during repr method test "
														   f"expected {expected} get {repr(triangle)} instead.")

	def test_eq(self):
		cases = [
			(self.t1, self.t2, False),
			(self.t1, self.t3, False),
			(self.t3, self.t2, False),
			(self.t4, self.t1, True),
			(self.t4, self.t2, False),
			(self.t4, self.t3, False),
			(self.t4, self.t4, True),
			(self.t3, self.t3, True),
			(self.t2, self.t2, True),
			(self.t1, self.t1, True),
		]

		for triangle1, triangle2, expected in cases:
			with self.subTest(triangle1=triangle1, triangle2=triangle2):
				self.assertEqual(triangle1 == triangle2, expected, msg=f"Failure during eq method test "
														   f"expected {expected} get {triangle1 == triangle2} instead.")

	def test_ne(self):
		cases = [
			(self.t1, self.t2, True),
			(self.t1, self.t3, True),
			(self.t3, self.t2, True),
			(self.t4, self.t1, False),
			(self.t4, self.t2, True),
			(self.t4, self.t3, True),
			(self.t4, self.t4, False),
			(self.t3, self.t3, False),
			(self.t2, self.t2, False),
			(self.t1, self.t1, False),
		]

		for triangle1, triangle2, expected in cases:
			with self.subTest(triangle1=triangle1, triangle2=triangle2):
				self.assertEqual(triangle1 != triangle2, expected, msg=f"Failure during ne method test "
														   f"expected {expected} get {triangle1 != triangle2} instead.")

	def test_center(self):
		cases = [
			(self.t1, Point(1.333, 0.667)),
			(self.t2, Point(2.333, 2.667)),
			(self.t3, Point(0.333, 3.667)),
		]

		for triangle, expected in cases:
			with self.subTest(triangle=triangle):
				self.assertAlmostEqual(triangle.center().x, expected.x, places=3,
									   msg=f"Failure during center method test"
										   f"expected x {expected.x} get {triangle.center().x} instead.")
				self.assertAlmostEqual(triangle.center().y, expected.y, places=3,
									   msg=f"Failure during center method test"
										   f"expected y {expected.y} get {triangle.center().y} instead.")

	def test_area(self):
		cases = [
			(self.t1, 3),
			(self.t2, 5.5),
			(self.t3, 12),
		]

		for triangle, expected in cases:
			with self.subTest(triangle=triangle):
				self.assertEqual((triangle.area()), expected, msg=f"Failure during area method test "
														   f"expected {expected} get {triangle.area()} instead.")

	def test_move(self):
		cases = [
			(self.t1, 1, 1, Triangle(1, 1, 4, 1, 2, 3)),
			(self.t2, -3, 8, Triangle(-2, 9, 1, 10, -1, 13)),
			(self.t3, -7, 10, Triangle(-9, 13, -7, 17, -4, 11)),
		]

		for triangle, move_x, move_y, expected in cases:
			with self.subTest(triangle=triangle, move_x=move_x, move_y=move_y):
				self.assertEqual((triangle.move(move_x, move_y)), expected, msg=f"Failure during move method test "
														   f"expected {expected} get {triangle.move(move_x, move_y)} instead.")
