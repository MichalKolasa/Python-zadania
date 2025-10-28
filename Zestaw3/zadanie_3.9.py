sequence = [[], [4], (1, 2), [3,4], (5, 6, 7)]
result = []

for item in sequence:
	result.append(sum(item))

expected_result = [0, 4, 3, 7, 18]
assert result == expected_result
print("TEST PASSED")