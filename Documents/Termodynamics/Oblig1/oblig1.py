from numpy import *
import math
import matplotlib.pyplot as mp

Na = 50 #number of states in A
Nb = 50 #number of states in B
q = 100 #energy avalible
omA = zeros(q+1)
omB = zeros(q+1)
omT = zeros(q+1)

for i in range(0,q+1):
    x = ( math.factorial((i+Na-1))/(math.factorial(i)*math.factorial((Na-1))))
    omA[i] = x
    y = (math.factorial(((q-i)+Nb-1))/(math.factorial((q-i))*math.factorial((Nb-1))))
    omB[i] = y
    omT[i] = (x*y)
    
#print omA, omB, omT
total = sum(omT) # total number of possibilities
print ('Probalility of all in B %g' %(omB[0]/total))
prob = zeros(q+1)
charg = zeros(q+1)
omT = array(omT)
for i in range(0,q+1):
    a = omT[i]/float(total)
    prob[i] = a
    charg[i] = i
    #print ('Number of parcels in A %.2f gives probability %.3f' %(i,prob[i])) 

mp.plot(charg,prob, 'r-')
mp.xlabel('Charges in A')
mp.ylabel('Probability of distribution')
mp.savefig('chdA.pdf', bbox_inches='tight')
mp.show()


