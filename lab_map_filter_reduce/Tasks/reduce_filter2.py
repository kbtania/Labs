# Дано масив (список) елементів цілого типу.
# Знайти суму додатних елементів.
from functools import reduce

count = int(input('Count el: '))
previous_list = [int(input('Enter element: ')) for x in range(count)]
positive_num = list(filter(lambda x: x > 0, previous_list))
positive_sum = reduce(lambda positive_sum, x: positive_sum + x, positive_num, 0)
print(positive_sum)
