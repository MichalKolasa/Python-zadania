# Funkcja iteracyjna obliczająca n-ty wyraz ciągu fibonacciego.
def fibonacci(n):
	if not isinstance(n, int):
		raise TypeError("Argument 'n' must be an integer.")
	if n < 0:
		raise ValueError("Argument 'n' must be non-negative.")

	a, b = 0, 1
	for _ in range(n): a, b = b, a + b

	return a

assert fibonacci(4) == 3
assert  fibonacci(12) == 144
print("TEST PASSED")