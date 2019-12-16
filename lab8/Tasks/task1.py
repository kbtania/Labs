from math import sin, cos
def suma(x):
    if x > 3:
        s = 0
        for i in range(1, 7):
            s += sin(x**i)
        return s
    else:
        z = -1
        s = 0
        a = cos(x)
        for i in range(1, 6):
            s = s + z*a
            a = cos(a)
            z = -z
        return s
num1 = int(input('a = '))
num2 = int(input('b = '))
print(min(suma(num1), suma(num2)))
