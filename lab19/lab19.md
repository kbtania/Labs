# ЛАБОРАТОРНА РОБОТА № 19

## Завдання 1

- Дано текстовий файл, який містить цілі числа. Визначити кількість елементів більших
за найменший елемент.

```py
with open('input_1_19.txt') as file:
    numbers = []
    for el in file:
        numbers.append(int(el))
    min_el = min(numbers)
    count_min = numbers.count(min_el)
    res = len(numbers) - count_min
    print(res)
```

## Завдання 2

- Дано типізований файл, який містить квадратну матрицю nnA (матриця
зберігається поелементно, кількість елементів визначити за допомогою функції FileSize).
Визначити найменший елемент серед додатних використовуючи динамічно створений
двовимірний масив. Від’ємні елементи зберегти у окремому файлі дійсних чисел «V.dat».

```py
with open('input_2_19.txt') as file:
    numbers = []
    file_list = []
    for el in file:
        file_list = file.read().splitlines()
    num_list = [int(j) for i in file_list for j in i.split()]
    count_el = len(num_list)
    print('Size of matrix is {0}x{1}'.format((count_el//2), (count_el//2)))

with open('output_2_19.txt', 'w') as f:
    negative_nums = [el for el in num_list if el < 0]
    for i in range(len(negative_nums)):
        f.write(str(negative_nums[i]))
```
