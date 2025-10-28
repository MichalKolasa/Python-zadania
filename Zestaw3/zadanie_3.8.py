# a)
# W zadaniu przyjmuje, że kolejne znaki/liczby są rozdzielone spacjami.
sequence1 = input("Enter first sequence: ")
sequence2 = input("Enter second sequence: ")

s1 = set(sequence1.split())
s2 = set(sequence2.split())
result = list(s1.intersection(s2))
print(result)

# b)
# Wykorzystuje sekwencje z podpunktu a)
result = s1.union(s2)
print(list(result))