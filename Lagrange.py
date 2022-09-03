import numpy as np

n = int(input('Enter the number of points'))

x = np.zeros((n))

y = np.zeros((n))

print('Enter the X and Y values: ')

for i in range(n):
    x[i] = float(input('x[' + str(i) + ']='))
    y[i] = float(input('y[' + str(i) + ']='))

xp = float(input('Enter the interpolation point: '))
yp = 0

for i in range(n):
    p = 1
    for j in range(n):
        if i != j:
            p = p * (xp - x[j]) / (x[i] - x[j])

    yp = yp + p * y[i]

print('The interpolation value at point %.3f is %.3f' % (xp, yp))