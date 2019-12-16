n=int(input('n = '))
x0=0
x1=9

if n==0:
    print(0)
elif n==1:
    print(9)
else:
    for i in range(n-1):
        xn=2*x1+3*x0
        x0=x1
        x1=xn
                    
    print('x(n) = {0}'.format(xn))
    



