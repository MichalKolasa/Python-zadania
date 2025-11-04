# Funkcja rekurencyjna obliczająca sumę liczb zawartych w sekwencji, mogącej
# zawierać zagnieżdżone podsekwencje.
def sum_seq(sequence):
	result = 0
	for item in sequence:
		if isinstance(item, (list, tuple)):
			result += sum_seq(item)
		else:
			result += item

	return result

assert sum_seq([1,(2,3),[],[4,(5,6,7)],8,[9]]) == 45
assert sum_seq([1,(23,3),[],[4,()]]) == 31