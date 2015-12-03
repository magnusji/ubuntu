from pylab import *
from numpy import *
import matplotlib.pyplot as mp
N = 10**23
deps = 1.0 #ev
kb = 8.617e-5 #eV/K Boltzmann
T = linspace(40,1000,100000)
rt = len(T)
n = zeros(rt)

for i in range(rt):
    n[i] = N*exp(-deps/(kb*T[i]))

print n
mp.plot(T,n)
mp.xlabel('Temperature')
mp.ylabel('Vacancies')

c = (deps**2*N/(kb*T**2))*exp(-deps/(kb*T))

mp.figure()
mp.plot(T,c)
mp.xlabel('Temperature ')
mp.ylabel('Heat capacity')
mp.show()
