#  Дано масив (список) елементів цілого типу.
#  Знайти добуток від’ємних елементів.
from functools import reduce
el_count = int(input('Element count: '))
some_list = [float(input('Enter element: ')) for x in range(el_count)]
negative_nums = list(filter(lambda x: x < 0, some_list))
if len(negative_nums) == 0:
    print('There are no negative numbers')
else:
    product = reduce((lambda product, x: product * x), negative_nums, 1)
    print(product)
