x = [float(input('Координата векора Х ')) for x in range(3)]
y = [float(input('Координата вектора Y ')) for x in range(3)]
x1 = x[1]*y[2]-x[2]*y[1]
y1 = x[2]*y[0]-x[0]*y[2]
z1 = x[0]*y[1]-x[1]*y[0]
print(x1, y1, z1)
