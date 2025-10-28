a = input("Enter rectangle height: ")
b = input("Enter rectangle width: ")
height = int(a)
width = int(b)

vertical = ["+" for i in range(width + 1)]
horizontal = ["|" for j in range(width + 1)]

print(height * ("---".join(vertical) + "\n" + "   ".join(horizontal) + "\n") +
	  "---".join(vertical))