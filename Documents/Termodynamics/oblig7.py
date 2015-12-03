from pylab import *


V_hat = linspace(0.4, 20, 200)
T_hat = [1.15, 1.0, 0.85]
rho = linspace(0.2,2.0, 10000)
'''
P_hat = zeros(200)
P_hat1 = ((8*T_hat[0])/(3*V_hat -1) ) -(3/V_hat**2)
P_hat2 = ((8*T_hat[1])/(3*V_hat -1) ) -(3/V_hat**2)
P_hat3 = ((8*T_hat[2])/(3*V_hat -1) ) -(3/V_hat**2)
'''

#print P_hat1
'''
figure(1)
plot(V_hat,P_hat1, 'b-', V_hat, P_hat2, 'r-', V_hat, P_hat3,'g-')
xlabel('Volume')
ylabel('Pressure')
'''
#---------------------------------#

#rho = linspace(0.0,2.0, 200)
P_rho1 = ((8*rho*T_hat[0])/(3-rho))-3*rho**2
P_rho2 = ((8*rho*T_hat[1])/(3-rho))-3*rho**2
P_rho3 = ((8*rho*T_hat[2])/(3-rho))-3*rho**2
'''
figure(2)

plot(rho,P_rho1, 'r-', rho, P_rho2,'g-', rho, P_rho3, 'b-')
xlabel('rho')
ylabel('Pressure')
'''

#-------------------------------------------#
figure()
#rho = linspace(0.2,2.0, 10000)
T = 0.9
'''
P_rho4 = zeros(len(rho))
g = zeros(len(rho))
'''
jlist = []

P_rho4 = ((8*rho*T)/(3-rho))-3*rho**2
g = -3*rho - (8.0/3.0)*T*log((3.0/rho) -1) + (P_rho4/rho)




for i in range(len(rho)):
    if P_rho4[i] >= 0.499 and P_rho4[i] <= 0.501:
        jlist.append(i)

indexi = []
indexj = []
for i in range(len(g)-1): 
    for j in range(i+1,len(g)): 
        if g[i] >= g[j]-0.00000001 and g[i] <= g[j] + 0.00000001: 
           indexi.append(i)
           indexj.append(j)

#print indexi
subplot(3,1,1)
plot(rho,P_rho4, 'b-')
xlabel('rho')
ylabel('Pressure')
title('Oblig 7 exercise k')
subplot(3,1,2)
plot(P_rho4, 1/rho,'b-')
xlabel('Pressure')
ylabel('Volume')
subplot(3,1,3)
plot(P_rho4, g,'b-')
xlabel('Pressure')
ylabel('Gibbs free energy')
subplot(3,1,1)
plot(rho[jlist],P_rho4[jlist], 'k*')
plot(rho[indexi], P_rho4[indexi], 'r-')
plot(rho[indexi], P_rho4[indexi], 'r*')
subplot(3,1,2)
plot(P_rho4[jlist], 1.0/rho[jlist], 'k*')
plot(P_rho4[indexi], 1.0/rho[indexi], 'r-')
plot(P_rho4[indexi], 1.0/rho[indexi], 'r*')
subplot(3,1,3)
#plot(P_rho4[jlist], g[jlist], 'r*')
plot(P_rho4[indexi], g[indexi], 'r-')
plot(P_rho4[indexi], g[indexi], 'r*')
#print j


show()
