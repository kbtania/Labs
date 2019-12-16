a = [int(input('Enter coordinates of vector a: ')) for x in range(3)]
b = [int(input('Enter coordinates of vector b: ')) for x in range(3)]
c = [int(input('Enter coordinates of vector c: ')) for x in range(3)]
b3 = list(map(lambda coordinate: coordinate * 3, b))  # b * 3
c2 = list(map(lambda coordinate: coordinate * 2, c))  # c * 2
a_3b = list(map(lambda x, y: x - y, a, b3))  # a - 3b
result = list(map(lambda x, y: x + y, a_3b, c2))  # a - 3b + 2c
print(result)
