nombres = [1, 21, 5, 44, 4, 9, 5, 83, 29, 31, 25, 38]
nombres_pairs = [i for i in nombres if i%2 == 0]
print(nombres_pairs)

nombres_positifs = [i for i in range(-10, 10) if i >= 0]
print(nombres_positifs)

nombres_doubles =[i * 2 for i in range(-10, 10)]
print(nombres_doubles)

nombres_inverses = [i if i%2 == 0 else -i for i in range(10)]
print(nombres_inverses)