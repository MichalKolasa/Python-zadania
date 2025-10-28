roman_dic = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
# Inne możliwości utworzenia słownika:
# 1) Dodając do pustego:
# roman_dic = {}
# roman_dic ['I'] = 1
# roman_dic ['V'] = 5
# roman_dic ['X'] = 10
# roman_dic ['L'] = 50
# roman_dic ['C'] = 100
# roman_dic ['D'] = 500
# roman_dic ['M'] = 1000

# 2) Za pomocą funkcji dict()
# roman_dic = dict(I=1, V=5, X=10, L=50, C=100, D=500, M=1000)

# 3) Za pomocą dwóch list i zip()
# keys = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
# values = [1, 5, 10, 50, 100, 500, 1000]
# roman_dic = dict(zip(keys, values))

# 4) Za pomocą listy krotek
# roman_dic = dict([('I', 1), ('V', 5), ('X', 10), ('L', 50), ('C', 100), ('D', 500), ('M', 1000)])