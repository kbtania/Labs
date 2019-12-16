from math import cos

i = int(input('i = '))
list_element = []
numerator = 1
denominator = 0
sum_positive = 0
sum_negative = 0
for x in range(1, i + 1):
    product = (2 * x - 1) * (cos(x))
    denominator += x ** 2
    numerator *= product
    element = numerator / denominator
    if element > 0:
        sum_positive += 1
    else:
        sum_negative += 1
    list_element.append(element)
if sum_negative < sum_positive:
    print(-1)
else:
    print(1)
