n=int(input('n= '))
a=float(input('a= '))
x=float(input('x= '))

s=(x+a)**2
for i in range(n-1):
    s=(s+a)**2
    
print('Sum = {0}'.format(s))
