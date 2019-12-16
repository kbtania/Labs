#  Дано масив (список) елементів цілого типу.
#  Знайти середнє арифметичне.
from functools import reduce
count = int(input('Element count: '))
some_list = [int(input('Enter element: ')) for x in range(count)]
suma = reduce(lambda suma, el: suma + el, some_list, 0)
aver = suma / len(some_list)
print(aver)
