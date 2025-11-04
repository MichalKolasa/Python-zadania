# Funkcja zwracająca spłaszczoną listę wszystkich elementów zadanej sekwencji,
# mogącej zawierać zagnieżdżone podsekwencje.
def flatten(sequence):
	result = []
	for item in sequence:
		if isinstance(item, (list, tuple)):
			result += flatten(item)
		else:
			result.append(item)

	return result

assert flatten([1,(2,3),[],[4,(5,6,7)],8,[9]]) == [1, 2, 3, 4, 5, 6, 7, 8, 9]
assert flatten([1,(23,3),[],[4,()]]) == [1, 23, 3, 4]
print("TESTS PASSED")