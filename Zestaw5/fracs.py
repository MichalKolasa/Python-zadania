from math import gcd

# Funkcja dodająca dwa ułamki do siebie zwraca wynik jako ułamek zapisany w formie
# kanonicznej w postaci listy [licznik, mianownik].
def add_frac(frac1, frac2):
	numerator1, denominator1 = frac1
	numerator2, denominator2 = frac2

	numerator = numerator1 * denominator2 + numerator2 * denominator1
	denominator = denominator1 * denominator2

	return simplify(numerator, denominator)

# Funkcja odejmująca dwa ułamki od siebie zwraca wynik jako ułamek zapisany w formie
# kanonicznej w postaci listy [licznik, mianownik] lub 0, jeśli jest wynikiem odejmowania.
def sub_frac(frac1, frac2):
	numerator1, denominator1 = frac1
	numerator2, denominator2 = frac2

	numerator = numerator1 * denominator2 - numerator2 * denominator1
	denominator = denominator1 * denominator2

	if is_zero([numerator, denominator]): return 0

	return simplify(numerator, denominator)

# Funkcja mnożąca dwa ułamki przez siebie zwraca wynik jako ułamek zapisany w formie
# kanonicznej w postaci listy [licznik, mianownik].
def mul_frac(frac1, frac2):
	numerator1, denominator1 = frac1
	numerator2, denominator2 = frac2

	numerator = numerator1 * numerator2
	denominator = denominator1 * denominator2

	return simplify(numerator, denominator)

# Funkcja dzieląca dwa ułamki przez siebie zwraca wynik jako ułamek zapisany w formie
# kanonicznej w postaci listy [licznik, mianownik].
def div_frac(frac1, frac2):
	numerator1, denominator1 = frac1
	numerator2, denominator2 = frac2

	numerator = numerator1 * denominator2
	denominator = denominator1 * numerator2

	return simplify(numerator, denominator)

# Funkcja sprawdzająca, czy ułamek jest dodatni.
def is_positive(frac):
	return frac2float(frac) > 0

# Funkcja sprawdzająca, czy ułamek nie jest zerem.
def is_zero(frac):
	return frac[0] == 0

# Funkcja porównująca dwa ułamki. Zwraca "-1" jeśli pierwszy jest mniejszy od drugiego,
# "0" jeśli ułamki są równe oraz "+1" jeśli pierwszy jest większy od drugiego.
def cmp_frac(frac1, frac2):
	numerator1, denominator1 = frac1
	numerator2, denominator2 = frac2

	# Ujednolicenie znaku mianownika
	if denominator1 < 0:
		numerator1, denominator1 = -numerator1, -denominator1
	if denominator2 < 0:
		numerator2, denominator2 = -numerator2, -denominator2

	numerator1 = numerator1 * denominator2
	numerator2 = numerator2 * denominator1

	if numerator1 < numerator2: return -1
	elif numerator1 > numerator2: return 1
	else: return 0


# Funckcja kowertująca ułamek zwykły na dziesiętny.
def frac2float(frac):
	numerator, denominator = frac
	dec = numerator / denominator

	return dec

# Funkcja pomocnicza do sprowadzania ułamka do postaci kanonicznej i korekcji
# znaku w razie potrzeby.
def simplify(nom, den):
	gcm = gcd(nom, den)
	nom = nom // gcm
	den = den // gcm

	if den < 0:
		nom = -nom
		den = -den

	return [nom, den]