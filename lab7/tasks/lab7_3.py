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
