# Cree un programa que ejecute una rutina desde
# 1 hasta un limite dado por el usuario
# en la rutina avance desde 1 hasta el limite de uno en uno
# Por cada numero si el numero es divisible entre 3 imprima fizz
# si el numero es divisible entre 5 imprima buzz
# si el numero es divisible entre 3 y 5 imprima fizzbuzz
# de lo contrario imprima el numero en si
# Limite: 15
# 1, 2, 'fizz', 4, 'buzz', 6...., 'fizzbuzz'
# y cree pruebas unitarias para validar el programa

from utils.fizzbuzz import fizzbuzz_sequence

limit = 15
result = fizzbuzz_sequence(limit)
for value in result:
    print(value)
