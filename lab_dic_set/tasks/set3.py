# Дано список цілих чисел. Створити функцію, яка повертає список з елементів, які не
# належать наперед заданій множині і не повторюються.
from random import randint

def check_num(num_list, checking):
    return set(num_list) - set(checking)

count = int(input('Count of numbers: '))
check_list = [randint(-5, 5) for x in range(count)]
numbers = [float(input('Enter number {0}'.format(x+1))) for x in range(count)]
print('Check list {0}'.format(check_list))
if len(check_num(numbers, check_list)) == 0:
    print('All numbers match to check list')
else:
    print('Numbers, that do not match to check list {0}'.format(check_num(numbers, check_list)))
