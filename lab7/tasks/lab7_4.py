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
