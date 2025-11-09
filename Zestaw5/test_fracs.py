import unittest
import fracs as fs

class TestFractions(unittest.TestCase):

    def setUp(self):
        self.zero = [0, 1]

    def test_add_frac(self):
        cases = [
            ([1, 2], [1, 3], [5, 6]),
            ([-1, 2], [1, 3], [-1, 6]),
            ([1, -2], [1, 3], [-1, 6]),
            ([-1, 2], [1, -6], [-2, 3]),
        ]

        for f1, f2, result in cases:
            with self.subTest(f1=f1, f2=f2):
                self.assertEqual(fs.add_frac(f1, f2), result,
                                 msg=f"Failure during addition test - test case {f1,f2}"
                                     f" expected {result} get {fs.add_frac(f1, f2)} instead.")


    def test_sub_frac(self):
        cases = [
            ([1, 2], [1, 3], [1, 6]),
            ([-1, 2], [1, 3], [-5, 6]),
            ([1, -2], [1, 3], [-5, 6]),
            ([-1, 2], [1, -6], [-1, 3]),
        ]

        for f1, f2, result in cases:
            with self.subTest(f1=f1, f2=f2):
                self.assertEqual(fs.sub_frac(f1, f2), result,
                                 msg=f"Failure during subtraction test - test case {f1,f2}"
                                     f" expected {result} get {fs.sub_frac(f1, f2)} instead.")


    def test_mul_frac(self):
        cases = [
            ([1, 2], [1, 3], [1, 6]),
            ([-1, 2], [1, 3], [-1, 6]),
            ([2, -2], [1, 3], [-1, 3]),
            ([-1, 2], [1, -6], [1, 12]),
        ]

        for f1, f2, result in cases:
            with self.subTest(f1=f1, f2=f2):
                self.assertEqual(fs.mul_frac(f1, f2), result,
                                 msg=f"Failure during multiplication test - test case {f1,f2}"
                                     f" expected {result} get {fs.mul_frac(f1, f2)} instead.")

    def test_div_frac(self):
        cases = [
            ([1, 2], [1, 3], [3, 2]),
            ([-1, 2], [1, 3], [-3, 2]),
            ([2, -2], [1, 3], [-3, 1]),
            ([-1, 2], [1, -6], [3, 1]),
        ]

        for f1, f2, result in cases:
            with self.subTest(f1=f1, f2=f2):
                self.assertEqual(fs.div_frac(f1, f2), result,
                                 msg=f"Failure during division test - test case {f1,f2}"
                                     f" expected {result} get {fs.div_frac(f1, f2)} instead.")


    def test_is_positive(self):
        cases = [
            ([-1, 6], False),
            ([1, -6], False),
            ([1, 6], True),
            ([0, 6], False),
        ]

        for f, result in cases:
            with self.subTest(f=f):
                self.assertEqual(fs.is_positive(f), result,
                                 msg=f"Failure during is_positive test - test case {f}"
                                     f" expected {result} get {fs.is_positive(f)} instead.")

    def test_is_zero(self):
        cases = [
            ([1, 6], False),
            ([-1, 6], False),
            ([1, -6], False),
            ([0, 6], True),
        ]

        for f, result in cases:
            with self.subTest(f=f):
                self.assertEqual(fs.is_zero(f), result,
                                 msg=f"Failure during is_zero test - test case {f}"
                                     f" expected {result} get {fs.is_zero(f)} instead.")

    def test_cmp_frac(self):
        cases = [
            ([1, 2], [1, 3], 1),
            ([-1, 2], [1, 3], -1),
            ([2, -2], [1, 3], -1),
            ([1, 2], [3, 6], 0),
        ]

        for f1, f2, result in cases:
            with self.subTest(f1=f1, f2=f2):
                self.assertEqual(fs.cmp_frac(f1, f2), result,
                                 msg=f"Failure during compare_frac test - test case {f1,f2}"
                                     f" expected {result} get {fs.cmp_frac(f1, f2)} instead.")

    def test_frac2float(self):
        cases = [
            ([1, 2], 0.5),
            ([1, 3], 0.3333333),
            ([8, 13], 0.6153846),
            ([-27, 4], -6.75),
        ]

        for f, result in cases:
            with self.subTest(f=f):
                self.assertAlmostEqual(fs.frac2float(f), result, places=7,
                                       msg=f"Failure during frac2float conversion test - test case {f}"
                                           f" expected {result} get {round(fs.frac2float(f), 7)} instead.")

    def tearDown(self): pass

if __name__ == '__main__':
    unittest.main()
