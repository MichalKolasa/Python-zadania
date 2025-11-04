# Wersja iteracyjna funkcji odwracającej listę od indeksu left do right włącznie.
def odwracanie_iter(L, left, right):
	while left < right:
		L[left], L[right] = L[right], L[left]
		left += 1
		right -= 1

	return L

# Wersja rekurencyjna funkcji odwracającej listę od indeksu left do right włącznie.
def odwracanie_rek(L, left, right):
	if left >= right:
		return L
	L[left], L[right] = L[right], L[left]

	return odwracanie_rek(L, left + 1, right - 1)


assert odwracanie_iter([1, 2, 3, 4, 5], 1, 3) == [1, 4, 3, 2, 5]
assert odwracanie_iter([1, 2, 3, 4, 5], 0, 4) == [5, 4, 3, 2, 1]
print("TEST 'odwracanie_iter' PASSED")
assert odwracanie_rek([1, 2, 3, 4, 5], 1, 3) == [1, 4, 3, 2, 5]
assert odwracanie_rek([1, 2, 3, 4, 5], 0, 4) == [5, 4, 3, 2, 1]
print("TEST 'odwracanie_rek' PASSED")
