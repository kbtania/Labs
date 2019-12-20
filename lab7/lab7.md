# ЛАБОРАТОРНА РОБОТА № 7

## Завдання 1

- Визначити добуток додатних елементів матриці вище головної діагоналі.

```py
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
```

## Завдання 2

- Дано дійсну матрицю розмірності nn , всі елементи якої різні. Знайти скалярний добуток i-го рядка і j-го стовпчика (i, j задаються користувачем).

```py
# Дано дійсну матрицю розмірності nxn , всі елементи якої різні.
# Знайти скалярний добуток i-го рядка і j-го стовпчика (i, j задаються користувачем).

n = int(input('Size of matrix: '))
matrix = [[int(input('El [{0}][{1}]: '.format(i, j))) for i in range(n)] for j in range(n)]
for el in matrix:
    print(el)
i = int(input('i row = '))
j = int(input('j column = '))
A = matrix[i]  # i-row
B = [row[j] for row in matrix]  # j-column
C = sum(a * b for a, b in zip(A, B))
print(C)
```

## Завдання 3

- Дано матриці A і B . Знайти матрицю AxB

```py
# Дано матриці А і В. Знайти С = АхВ

i1 = int(input('Rows 1: '))  # count of rows in 1 matrix
j1 = int(input('Columns 1: '))  # count of columns in 1 matrix
i2 = int(input('Rows 2: '))  # count of rows in 2 matrix
j2 = int(input('Columns2: '))  # count of columns in 2 matrix

if j1 == i2:
    A = [[int(input('El [{0}][{1}]: '.format(i, j))) for i in range(j1)] for j in range(i1)]
    for t in A:
        print(t)
    B = [[int(input('El [{0}][{1}]: '.format(x, y))) for x in range(j2)] for y in range(i2)]
    for q in B:
        print(q)
    result = [[0 for x in range(j2)] for y in range(i1)]
    for i in range(len(A)):  # iterate through rows of A
        for j in range(len(B[0])):  # iterate through columns of B
            for k in range(len(B)):  # iterate through rows of B
                result[i][j] += A[i][k] * B[k][j]
    for r in result:
        print(r)
else:
    print('Wrong size of matrices')
```

## Завдання 4

- Розмістити елементи непарних стовпців у порядку зростання.

```py
#  Розмістити елементи непарних стовпців у порядку зростання.

size = int(input('Size of matrix = '))
matrix = [[int(input("El {0},{1} = ".format(i, j))) for j in range(size)] for i in range(size)]
print('Original matrix')
for row in matrix:
    print(row)

transposed_matrix = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix))]
res = []
for row in transposed_matrix:
    if transposed_matrix.index(row) % 2 == 0:
        res.append(sorted(row))

    if transposed_matrix.index(row) % 2 != 0:
        res.append(row)

print('Sorted matrix ')
transposed_res = [[res[j][i] for j in range(len(res))] for i in range(len(res))]
for t in transposed_res:
    print(t)
```

## Завдання 5

- Дана цілочислова квадратна матриця. Визначити добуток елементів в тих рядках, які не
містять від’ємних елементів.

```py
# Дана цілочислова квадратна матриця. Визначити добуток елементів в тих рядках, які не
# містять від’ємних елементів.

from functools import reduce
size = int(input('Size of matrix: '))
matrix = [[int(input('El {0},{1}: '.format(x, y))) for x in range(size)] for y in range(size)]
for row in matrix:
    if len([element for element in row if element > 0]) == len(matrix):  # check rows
        result = reduce(lambda x, y: x * y, row)
        print('Product of {0} = {1}'.format(row, result))
```

## Завдання 6

- Дана цілочислова квадратна матриця. Визначити максимум серед сум елементів
діагоналей, паралельних головній діагоналі матриці.

```py
#  Дана цілочислова квадратна матриця. Визначити максимум серед сум елементів
#  діагоналей, паралельних головній діагоналі матриці.

size = int(input('Size of matrix: '))
mat = [[int(input('Element: ')) for x in range(size)] for y in range(size)]
for row in mat:
    print(row)
for i in range(size):
    for j in range(size):
        mat[i].reverse()
n = len(mat)
res = [[mat[y-x][x] for x in range(n) if 0 <= y - x < n] for y in range(2*n-1)]
sum_list = []
for el in res:
    sum_list.append(sum(el))
print('Max of sums ', max(sum_list))
```

