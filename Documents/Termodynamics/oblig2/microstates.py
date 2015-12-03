from pylab import *

N = 50  
S = 10000
m = randint(-1,2,(N,S))
print(m[0:5,:])
n = sum(m, axis=1)
hist(n)

hold('on')
sn = linspace(-300,300,10000)
plot(sn,exp(-2*sn**2/N), 'r-')
show()
    
