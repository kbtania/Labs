# ЛАБОРАТОРНА РОБОТА № 10

## Завдання 1

| **Клас** | **Трикутник** |
| ------ | ------ |
| **Поля** | для зберігання довжин сторін; |
| **Методи** | конструктор без параметрів, конструктор з параметрами, конструкторкопіювання; |
|    | введення/виведення даних; |
|    | визначення площі; |
|    | визначення периметру; |
|    | порівняння з іншим трикутником; |
|    | перевантаження операторів + (додавання довжин сторін), – (віднімання довжин відповідних сторін), * (множення сторін на деяке число).|


```py
from math import sqrt

class Triangle:
    def __init__(self, a, b, c):
        if a < 0 or b < 0 or c < 0:
            raise Exception('Side cannot be negative')
        self.a = a
        self.b = b
        self.c = c

    def set_side(self):
        self.a = int(input('Side a = '))
        self.b = int(input('Side b = '))
        self.c = int(input('Side c = '))
        return self.a, self.b, self.c

    def get_side(self):
        return self.a, self.b, self.c

    def get_square(self):
        p = (self.a + self.b + self.c) / 2
        return sqrt(p*(p-self.a)*(p-self.b)*(p-self.c))

    def get_perimeter(self):
        return self.a + self.b + self.c

    def __add__(self, other):
        return Triangle(self.a + other, self.b + other, self.c + other)

    def __sub__(self, other):
        return Triangle(self.a - other, self.b - other, self.c - other)

    def __mul__(self, other):
        return Triangle(self.a * other, self.b * other, self.c * other)

    def __str__(self):
        return "Sides are {0}, {1}, {2}".format(self.a, self.b, self.c)


num = int(input('Enter some num: '))
tr1 = Triangle(3, 4, 5)
print('Sides of triangle are {0}'.format(tr1.get_side()))
print('Perimeter of triangle is {0}'.format(tr1.get_perimeter()))
print('Square of triangle is {0}'.format(tr1.get_square()))
print(' Add {0}: {1}'.format(num, tr1 + num))
```
