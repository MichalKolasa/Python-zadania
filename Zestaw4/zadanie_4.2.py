input_data = input("Enter ruler length: ")
length = int(input_data)

# Funkcja tworząca linijkę o zadanej długości n
def make_ruler(n):
	if not isinstance(n, int):
		raise TypeError("Argument 'n' must be an integer.")
	if n < 0:
		raise ValueError("Argument 'n' must be non-negative.")

	ruler = ["|" for _ in range(n + 1)]
	graduation = []

	for i in range(n + 1):
		number = str(i)
		segment_len = 5 - len(number)

		if i == 0:
			graduation.append(number)
		else:
			graduation.append(" " * segment_len + number)

	return "....".join(ruler) + "\n" + "".join(graduation)

print(make_ruler(length))


a = input("Enter rectangle height: ")
b = input("Enter rectangle width: ")
height = int(a)
width = int(b)

# Funkcja tworząca prostokąt o zadanych wymiarach: rows - wysokość, cols - szerokość
def make_grid(rows, cols):
	if not isinstance(rows, int) or not isinstance(cols, int):
		raise TypeError("Arguments must be an integers.")
	if rows < 0 or cols < 0:
		raise ValueError("Arguments must be non-negative.")

	vertical = ["+" for _ in range(cols + 1)]
	horizontal = ["|" for _ in range(cols + 1)]

	return (rows * ("---".join(vertical) + "\n" + "   ".join(horizontal) + "\n") +
		"---".join(vertical))

print(make_grid(height, width))