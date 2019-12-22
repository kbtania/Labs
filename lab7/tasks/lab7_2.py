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
