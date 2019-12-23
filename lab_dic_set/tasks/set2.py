# Дано два списки чисел. Виведіть всі числа, які входять як в перший,
# так і в другий список в порядку зростання.

num_list1 = [float(input('Enter number {0}: '.format(x+1))) for x in range(5)]
num_list2 = [float(input('Enter number {0}: '.format(x+1))) for x in range(5)]
result = sorted((set(num_list1) & set(num_list2)))
if len(result) > 0:
    print(result)
else:
    print('No element is in both of those lists')