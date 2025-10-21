# String line wykorzystywany do testowania rozwiązań:
line = """
GvR once said
   Code is read more often than it is written
And with that a language was born
"""
# Zadanie 2.10
print("#ZADANIE 2.10")
print(len(line.split()))

# Zadanie 2.11
print("\n#ZADANIE 2.11")
print("_".join("word"))

# Zadanie 2.12
print("\n#ZADANIE 2.12")
first_chars = "".join(word[0] for word in line.split())
last_chars = "".join(word[-1] for word in line.split())
print(f"Z pierwszych znaków: {first_chars}, z ostatnich: {last_chars}.")

# Zadanie 2.13
print("\n#ZADANIE 2.13")
words = line.split()
print(sum(len(i) for i in words))

# Zadanie 2.14
# Korzystam z listy words utworzonej w zadaniu poprzednim
print("\n#ZADANIE 2.14")
longest_word = max(word for word in words)
longest_word_lenght = max(len(word) for word in words)
print(f"Najdłuższe słowo: {longest_word} , długość: {longest_word_lenght}.")

# Zadanie 2.15
print("\n#ZADANIE 2.15")
L = [1, 7, 12, 15, 27]
s = "".join(str(n) for n in L)
print(s)

# Zadanie 2.16
print("\n#ZADANIE 2.16")
line = line.replace("GvR", "Guido van Rossum")
print(line)

# Zadanie 2.17
print("\n#ZADANIE 2.17")
words = line.split()
words_sorted_alf = sorted(words, key=str.lower)
words_sorted_by_lenght = sorted(words, key=len)
print(words_sorted_alf)
print(words_sorted_by_lenght)

# Zadanie 2.18
print("\n#ZADANIE 2.18")
number = 100050008000
print(str(number).count("0"))

# Zadanie 2.19
print("\n#ZADANIE 2.19")
L = [1, 7, 12, 15, 124, 333]
print("".join(list(str(i).zfill(3) for i in L)))

