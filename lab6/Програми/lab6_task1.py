n = int(input('Кількість чисел: '))
numbers = [float(input('Число = ')) for x in range(n)]
minim = numbers[0]
for x in numbers:
    if x < minim:
        minim = x
print('Найменше число = {0}'.format(minim))
