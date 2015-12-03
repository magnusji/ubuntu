from numpy import *
from matplotlib.pyplot import *

class Readdata():
    def __init__(self,filename):
        self.infile = open(filename,'r'); #self.infile.readlines();

    def set_var(self): 
        self.Date = []; self.Latitude = []; self.Longitude = [];
        for line in self.infile:
            words = line.split()
            self.Date.append(words[1]); self.Latitude.append(words[4]); self.Longitude.append(words[5]);
    
    def distance(self):
        self.SvalbardLat = radians(78.15); self.Svalbardlong = radians(16.04); 
        self.latdist = []; self.longdist = [];
        for i in range(len(self.Latitude)):
            self.latdist[i] = abs(self.Svalbardlat-radians(self.Latitude[i]))
            self.longdist[i] = abs(self.Svalbardlat-radians(self.Longitude[i]))
            
        




a = Readdata('./Data/SW_PREL_EFIA_LP_1B_20131229T000000_20131229T235959_0102.txt') ;  a.set_var()
    
#print Latitude
plot(a.Longitude,a.Latitude, 'b-', 16.04,78.15, 'r*')
show()                        

