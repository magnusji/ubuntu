'''

 1     I4       Year                                1976, 1977, etc. 
    2     I4       Decimal Day                           January 1 = Day 1 
    3     I3       Hour                                   0, 1, ... 23
    4     I5       Carrington Rotation Number        Seen by an Earth based
                                                     observer at the start 
                                                     of the data interval 
    5     F7.2     Spacecraft Heliocentric             astronomical units
                   Distance

    6     F7.1     Heliographic Inertial Latitude        degrees, +/- 90
                   of the spacecraft position
                   at the start of data interval
                   
    7     F7.1     Heliographic Inertial Longitude       degrees, 0-360
                   of the spacecraft position
                   at the start of data interval
                         
    8     F7.1     Earth - Sun - Spacecraft              degrees, 0-360 
                   separation angle
                          
    9     F9.2     BX in SSE coordinate system           nanoteslas
                   
   10     F9.2     BY in SSE coordinate system           nanoteslas 
                          
   11     F9.2     BZ in SSE coordinate system           nanoteslas
                     
   12     F9.2     BR in RTN coordinate system           nanoteslas
                      
   13     F9.2     BT in RTN coordinate system           nanoteslas
                     
   14     F9.2     BN in RTN coordinate system           nanoteslas
                       
   15     F9.2     Scalar B (avg of fine scale           nanoteslas 
                      magnitudes)
 
   16     F7.1     Solar wind bulk flow speed              km/s  
                          
   17     F7.1     Flow elevation angle (RTN)     degrees +/- 90
                               
   18     F7.1     Flow azimuth angle (RTN)       degrees, +/-180
                           
   19     F6.1     Solar wind proton density             protons/cm3 

   20     F9.0     Radial component of the proton        degrees, K
                   temperature                        
                                
'''
from numpy import *
from scipy import *
import matplotlib.pyplot as mp
import datetime

#constants
kb = 1.38e-23 #Boltzmann
pm = 1.67e-27 # proton mass

#reading file
infile = open('helios1_daily.dat','r')

year = []; desdate = []; hours = []; crn = []; schsd = []; temp = []; bfspeed = []; scB = []
for line in infile:
    columns =map(float, line.split())
    year.append(columns[0])
    desdate.append(columns[1])
    hours.append(columns[2])
    crn.append(columns[3])
    schsd.append(columns[4])
    scB.append(columns[14])
    bfspeed.append(columns[15])
    temp.append(columns[-1])
infile.close()

#creating putting together year and day of year as time
n = int(len(year))
date = []
cs = zeros(n)
mach = zeros(n)
tb3 = zeros(n)
tb32 = zeros(n)
for i in range(n):
    y = int(year[i])
    d = int(desdate[i])
    da = datetime.date(y,1,1) + datetime.timedelta(d-1)
    cs[i] = sqrt(2*kb*temp[i]/pm)
    mach[i] = bfspeed[i]*10**3/cs[i]
    tb3[i] = scB[i]*schsd[i]**3
    tb32[i] = scB[i]*schsd[i]**(3/2.0)
    date.append(da)



'''
mp.figure()
mp.plot(date,schsd)
mp.xlabel('Time [year]')
mp.ylabel('Heliocentric distance')

mp.figure()
mp.plot(date,temp)
mp.xlabel('Time')
mp.ylabel('Temperature K')

mp.figure()
mp.plot(schsd, temp)
mp.xlabel('Heliocentric distance')
mp.ylabel('Temperature K')


mp.figure()
mp.plot(date,cs)
mp.xlabel('Time')
mp.ylabel('Soundspeed')

mp.figure()
mp.plot(schsd,mach,'b+')
mp.xlabel('Heliocentric distance')
mp.ylabel('Mach number')
'''

mp.figure()
mp.plot(schsd,tb3,'b+')
mp.xlabel('Heliocentric distance')
mp.ylabel('TB3')


mp.figure()
mp.plot(schsd,tb32,'b+')
mp.xlabel('Heliocentric distance')
mp.ylabel('TB3/2')


mp.show()

    
