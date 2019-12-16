from math import log

accuracy = float(input('Введіть точність: '))
a = float(input('Введіть а: '))
x = float(input('Введіть х: '))
suma = 1
n = 1
f = 1
while True:
    next_addition = abs(((x*log(a))**n)/f)
    if next_addition >= accuracy:
        suma += next_addition
        n += 1
        f *= n              
    else:
        break
print('Сума = {0}'.format(suma))
   
