from numpy import *
import matplotlib.pyplot as mp
import math

N = 1000000
S = zeros(N)
T = linspace(0.01, 100, N)
for i in range(N-1):
    S[i] = math.tanh(1./T[i])

mp.plot(T,S)
mp.show()
