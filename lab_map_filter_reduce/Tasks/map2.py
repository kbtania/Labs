#  Дано два вектори (списки з координатами – дійсними числами).
#  Зясувати, чи є вектори перпендикулярними.
vector1 = [float(input('Coordinate of vector 1: ')) for x in range(3)]
vector2 = [float(input('Coordinate of vector 2: ')) for x in range(3)]
coordinate_product = list(map(lambda x1, x2: x1 + x2, vector1, vector2))
if sum(coordinate_product) == 0:
    print('Perpendicular')
else:
    print('No')
