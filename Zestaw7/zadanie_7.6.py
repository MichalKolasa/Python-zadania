import itertools
import random

# Iteratory nieskończone:

# a) zwracający 0, 1, 0, 1, 0, 1, ...
it_zeros_ones = itertools.cycle([0, 1])

print(next(it_zeros_ones))
print(next(it_zeros_ones))
print(next(it_zeros_ones))
print(next(it_zeros_ones))

# b) zwracający przypadkowo jedną wartość z ("N", "E", "S", "W") [błądzenie przypadkowe na sieci kwadratowej 2D]
directions = ["N", "E", "S", "W"]
it_random_walk = iter(lambda: random.choice(directions), None)

print(next(it_random_walk))
print(next(it_random_walk))
print(next(it_random_walk))
print(next(it_random_walk))

# c) zwracający 0, 1, 2, 3, 4, 5, 6, 0, 1, 2, 3, 4, 5, 6, ... [numery dni tygodnia]
it_days = itertools.cycle(list(range(7)))

print(next(it_days))
print(next(it_days))
print(next(it_days))
print(next(it_days))
print(next(it_days))
print(next(it_days))
print(next(it_days))
print(next(it_days))