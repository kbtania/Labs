'''Визначення найменшої цифри в числі'''

number = int(input('Введіть число: '))
minim = 10
while number>0:
    if number%10 < minim:
        minim = number%10
    number = number//10
print('Найменша цифра = {0}'.format(minim))
