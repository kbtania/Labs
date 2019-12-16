#  Дано масив (список) елементів цілого типу.
#  Підрахувати кількість елементів, які більші за середнє арифметичне.
from functools import reduce
count = int(input('Element count: '))
some_list = [int(input('Enter element: ')) for x in range(count)]
suma = reduce((lambda suma, el: suma + el), some_list, 0)
aver = suma / len(some_list)
res = len(list(filter(lambda el: el > aver, some_list)))
print(res)
