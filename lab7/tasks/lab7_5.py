# Дана цілочислова квадратна матриця. Визначити добуток елементів в тих рядках, які не
# містять від’ємних елементів.

from functools import reduce
size = int(input('Size of matrix: '))
matrix = [[int(input('El {0},{1}: '.format(x, y))) for x in range(size)] for y in range(size)]
for row in matrix:
    if len([element for element in row if element > 0]) == len(matrix):  # check rows
        result = reduce(lambda x, y: x * y, row)
        print('Product of {0} = {1}'.format(row, result))
