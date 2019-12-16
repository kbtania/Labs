# Дано два вектори (списки з координатами – дійсними числами).
# Знайти суму векторів.

vector1 = [float(input('Coordinate of vector1: ')) for x in range(3)]
vector2 = [float(input('Coordinate of vector2: ')) for x in range(3)]
sum_vector = map(lambda x, y : x + y, vector1, vector2)
print(list(sum_vector))