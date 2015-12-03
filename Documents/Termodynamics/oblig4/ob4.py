from pylab import *
from numpy import *

Tmarked = [0.05, 0.2, 5, 10 , 15, 20]
n = 100
lT = len(Tmarked)-1
z = zeros((lT,n), 'float')
for i in range(lT):
    for j in range(n):
        z[i,j] = (2.0*j+1)*exp(-(j*(j+1))*Tmarked[i])
        print j



t = linspace(0,5,n)

hold('on')
for i in range(lT):
    plot(t,z[i,:])

show()
