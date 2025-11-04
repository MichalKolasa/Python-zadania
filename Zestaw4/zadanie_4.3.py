from functools import reduce

# Funkcja iteracyjna obliczająca silnię z liczby n
def factorial(n):
	if not isinstance(n, int):
		raise TypeError("Argument 'n' must be an integer.")
	if n < 0:
		raise ValueError("Argument 'n' must be non-negative.")

	if n in (0, 1):
		return 1

	return reduce(lambda x, y: x*y, range(2, n+1))

assert factorial(5) == 120
assert factorial(10) == 3628800
print("TESTS PASSED")
