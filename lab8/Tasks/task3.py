i = int(input('i = '))

def recurs(i):
    if i == 0 or i == 1:
        return 1
    else:
        return recurs(i-1) + 2*recurs(i-2)

print('i({0}) = {1}'.format(i, recurs(i)))
