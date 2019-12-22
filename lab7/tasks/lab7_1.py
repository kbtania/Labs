#  Дана цілочислова матриця.
#  Визначити добуток додатних елементів матриці вище головної діагоналі.

n = int(input('Rows: '))
matrix = [
    [int(input('Element: ')) for i in range(n)] for j in range(n)
]
for el in matrix:
    print(el)
product = 1
for j in range(n):
    for i in range(n):
        if j < i and matrix[j][i] > 0:
            product *= matrix[j][i]
print(product)
