import numpy as np
import os


#---------------------------------------#
'''
reading data from data file ascii type  
'''
sat, Date, Day2000, Msec, Latitude, Longitude, Height, Radius, Sza, Azimuth, Ne, Te, Vs, Flag = np.genfromtxt('./Data/SW_PREL_EFIA_LP_1B_20131229T000000_20131229T235959_0102.txt')

print Day2000

'''
with  open('./Data/SW_PREL_EFIA_LP_1B_20131229T000000_20131229T235959_0102.txt', 'r') as infile:
    data = infile.read()

columns = data.splitlines()
print(columns[1])

'''
'''
dtype={'names':('sat', 'Date', 'Day2000', 'Msec', 'Latitude', 'Longitude', 'Height', 'Radius', 'Sza', 'Azimuth', 'Ne', 'Te', 'Vs', 'Flag')},
'''
