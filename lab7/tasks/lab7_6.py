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
