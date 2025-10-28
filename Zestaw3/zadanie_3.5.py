input_data = input("Enter ruler length: ")

length = int(input_data)
ruler = ["|" for i in range(length + 1)]
graduation = []

for i in range(length + 1):
	number = str(i)
	segment_len = 5 - len(number)

	if i == 0:
		graduation.append(number)
	else:
		graduation.append(" " * segment_len + number)

print("....".join(ruler) + "\n" + "".join(graduation))


