#! /usr/bin/python

''' This is a script where an effort is made in order to choose the stations that are effected by an earthquake.
    For this reason, two equations are used, where the second one is +0.8 magnitudes higher than the first one. The first equation 
    is according to Delle Donne et al. and the second one, is the equation running in FODITS extension of Bernese Software. '''
    
import sys, os
import datetime
import math

Stacoord_list = []
Merq1_list = []
Merq2_list = []

def read_sta_file(sta):
    
    with open(sta, 'r') as buf:
        line = buf.readline()
        
        for line in buf.readline():
            try:
                st = Stacoord(line)
                Stacoord_list.append(st)
            except:
                print 'Invalid line: [%s]; line skipped'%(line)
        line = buf.readline()                                                     
    
''' In this step, the distance derq is given by stations coordinates X and Y from sta_list, and coordinates of earthquake epicenter
    are given by the user. Next step, the equations for choosing the stations. Equation Merq1 is according to Delle Donne and Merq2 
    is used by FODITS. Muser is the magnitude given by the user.'''
    
def dist_sta(sta_list):
    derq = 0
    Merq1 = 0
    Merq2 = 0
    Muser = float(raw_input('Enter magnitude of earthquake'))
    X_epi = float(raw_input('Enter X coordinate of epicenter'))
    Y_epi = float(raw_input('Enter Y coordinate of epicenter'))
    Z_epi = float(raw_input('Enter Z coordinate of epicenter'))
                    
    for i in sta_list():
        derq = sqrt(pow((X_epi - i.x()), 2) + pow((Y_epi - i_y()), 2) + pow((Z_epi - i.z()), 2)) 
        Merq1 = -6.40 + 2.17 * log10(derq)
        Merq2 = -5.60 + 2.17 * log10(derq)
        sta = Station_list(l[0], float(l[1]), float(l[2]), float(l[3]))
        
        if Muser >= Merq1:
            Merq1_list.append(sta)
        else :
            Merq2_list.append(sta)
            
    return 

class Station_list:

    def __init__(self, line):
        try:
            l = line.split()
            self.sta_name = l[0]
            self.m_x = float(l[1])
            self.m_y = float(l[2])
            self.m_z = float(l[3])
        except:
            raise RuntimeError('Invalid line [%s]'%line)
        
   def sta_name(self):
       return self.sta_name
   
   def x(self):
       return self.m_x
   
   def y(self):
       return self.m_y
   
   def z(self):
       return self.m_z      
       
read_sta_file(sys.argv[1])
derq = dist_sta(Stacoord_list)
print ' Station distance from the epicenter is %10.3f =' %(derq)
Merq1 = dist_sta(Stacoord_list)
Merq2 = dist_sta(Stacoord_list)
print 'Muser is %10.3f = ' %(Muser)
print 'X_epi is %10.3f = ' %(X_epi)
print 'Y_epi is %10.3f = ' %(Y_epi)
print 'Z_epi is %10.3f = ' %(Z_epi)

