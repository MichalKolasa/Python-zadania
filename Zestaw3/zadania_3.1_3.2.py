# ZADANIE 3.1
# a)
# Kod jest poprawny, ale posiada zbędne średniki na końcu lini. Podobnie nawiasy
# w warunku if są niepotrzebne.
x = 2; y = 3;
if (x > y):
	result = x;
else:
	result = y;

# b)
# Kod jest niepoprawny. W pythonie nie możemy zastosować składni odpowiadającej
# for ...; if ... w języku C.

# for i in "axby": if ord(i) < 100: print (i) - błędne

# Najprościej naprawić to umieszczając warunek z if w nowej lini:
for i in "axby":
	if ord(i) < 100: print(i)

# c)
# Kod jest poprawny.
for i in "axby": print (ord(i) if ord(i) < 100 else i)

# ZADANIE 3.2
# a)
L = [3, 5, 4]
# L = L.sort() - to dam nam None, bo L.sort() nie tworzy nowej listy tylko pracuje
#                na liście L samo w sobie zwracając None
L.sort() # poprawna wersja

# b)
# x, y = 1, 2, 3 - błędne bo mamy dwie zmienne, do których chcemy przypisać trzy
#                  wartości
# Poprawana wersja - potrzebujemy trzech zmiennych
x, y, z = 1, 2, 3

# c)
# X = 1, 2, 3; X[1] = 4 - błędne bo nie możemy modyfikować krotek

# d)
# X = [1, 2, 3] ; X[3] = 4 - błędne bo wstawiamy 4 pod nieistniejący indeks - spoza zakresu

# e)
# X = "abc"; X.append("d") - błędne bo metoda append() nie działa dla stringów, należałoby użyć metody join()

# f)
#L = list(map(pow, range(8))) - błędne bo do funkcji map() podajemy za mało argumentów,
#                               przez co nie mamy jak obliczać kolejnych potęg (brakuje wykładników)

