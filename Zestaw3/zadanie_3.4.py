while True:
	input_data = input("Enter any number: ")

	if input_data == "stop":
		break
	try:
		number = float(input_data)
	except ValueError:
		print("Is not a number!!!")
	else:
		print(f"{number}, {number**3}")