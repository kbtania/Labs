# Лабораторна робота. Словники. Множини.

## Завдання 1

#### Дано інформацію про відвідувачів деякого сайту (для кожного відвідувача зберігається  логін). Підрахувати для кожного клієнта кількість відвідувань.

```py
user_count = int(input('General amount of users: '))
user_dic = {i: input('Enter log of user: ') for i in range(user_count)}
log_list = list(user_dic.values())
res = {i: log_list.count(i) for i in log_list}
print(res)
```

## Завдання 2

#### Дано список імен студентів в межах групи. З’ясувати чи є серед них тезки.

```py
students_count = int(input('General amount of students: '))
students_dic = {i: input('Enter name of student: ') for i in range(students_count)}
name_list = list(students_dic.values())
if len(set(name_list)) == len(name_list):
    print('Everyone has different name')
else:
    print('Some students have the same name')
```

## Завдання 3

#### Дано рядок символів. З’ясувати скільки серед вказаних символів є таких, які повторюються

```py
symbols = input('Enter some text: ')
unique_count = len(symbols) - len(set(symbols))
print(unique_count)
```

## Завдання 4

#### Дано два списки чисел. Виведіть всі числа, які входять як в перший, так і в другий список в порядку зростання.

```py
num_list1 = [float(input('Enter number {0}: '.format(x+1))) for x in range(5)]
num_list2 = [float(input('Enter number {0}: '.format(x+1))) for x in range(5)]
result = sorted((set(num_list1) & set(num_list2)))
if len(result) > 0:
    print(result)
else:
    print('No element is in both of those lists')
```

## Завдання 5

#### Дано список цілих чисел. Створити функцію, яка повертає список з елементів, які не належать наперед заданій множині і не повторюються.

```py
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
```
