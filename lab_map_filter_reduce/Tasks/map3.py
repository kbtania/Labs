#  Дано два вектори (списки з координатами – дійсними числами). Знайти
#  скалярний добуток векторів

vector1 = [float(input('Coordinate of vector 1: ')) for x in range(3)]
vector2 = [float(input('Coordinate of vector 2: ')) for x in range(3)]
scalar_product = sum(list(map(lambda x, y: x * y, vector1, vector2)))
print(scalar_product)