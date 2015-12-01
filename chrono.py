#! /usr/bin/python

import sys
import datetime
import numpy as np

CoordRec_list = []

def read_cts_file(ct):

    with open(ct, 'r') as buf:
        line = buf.readline()
        
        while line:
            if line[0] == "#":
                pass
            else:
                try:
                    cr = CoordRec(line)
                    CoordRec_list.append(cr)
                except:
                    print 'Invalid line: [%s]; line skipped'%(line)
            line = buf.readline()

#s0 is set to be equal to 1
#Trying to adjust the optimal line (type : y = a*x + b) in data.

#def optimal_line(cr_list):
#    C = np.array(cr_list)
#    l = 0
#    A = 0
#    P = np.identity(6, dtype = float)
#    for i in cr_list:
#        l = l + np.array([i.y()], dtype = float)
#        A = A + np.array([i.x(), 1], dtype = float)
#        P = P * (1/i.sx())
    
    #l = C[5]
        
def matrix_A(cr_list):
    A = 0 
    for i in cr_list:
#        A = A + np.append([i.x(), 1],[i.x(), 1], axis = 0)
        A = A + np.array([i.x(), 1], float)
    return A

def compute_average_x(cr_list):
    sum_of_x = 0
    Pi = 0
    for i in cr_list:
        sum_of_x = sum_of_x + (i.x() * ( 1 / i.sx()))
        Pi = Pi + ( 1 / i.sx())
    return sum_of_x / Pi 

def compute_average_y(cr_list):
    sum_of_y = 0
    Pi = 0
    for i in cr_list:
        sum_of_y = sum_of_y + (i.y() * (1 / i.sy()))
        Pi = Pi + ( 1 / i.sy())
    return sum_of_y / Pi

def compute_average_z(cr_list):
    sum_of_z = 0
    Pi = 0
    for i in cr_list:
        sum_of_z = sum_of_z + (i.z() * (1 / i.sz()))
        Pi = Pi + ( 1 / i.sz())
    return sum_of_z / Pi

class CoordRec:

    def __init__(self, line):
        ## print 'calling CoordRec::__init__(self, %s)'%(line)
        try:
            l = line.split()
            self.m_time = datetime.datetime(int(l[0]), int(l[2]), int(l[3]))
            self.m_x  = float(l[4])
            self.m_y  = float(l[5])
            self.m_z  = float(l[6])
            self.m_sx = float(l[7])
            self.m_sy = float(l[8])
            self.m_sz = float(l[9])
        except:
            raise RuntimeError('Invalid line [%s]'%line)
        ## print 'Constructed new CoordRec, with x=%10.3f, y=%10.3f, z=%10.3f'%(self.m_x, self.m_y, self.m_z)

    def x(self):
        return self.m_x
    
    def y(self):
        return self.m_y
    
    def z(self):
        return self.m_z
    
    def sx(self):
        return self.m_sx
    
    def sy(self):
        return self.m_sy
     
    def sz(self):
        return self.m_sz
    
#ctsfile = sys.argv[1]
read_cts_file(sys.argv[1])
print 'I have read %i elements'%(len(CoordRec_list))
x_mean = compute_average_x(CoordRec_list)
print 'Average value of x = %10.3f'%(x_mean)
y_mean = compute_average_y(CoordRec_list)
print 'Average value of y = %10.3f'%(y_mean)
z_mean = compute_average_z(CoordRec_list)
print 'Average value of z = %10.3f'%(z_mean)
#l = optimal_line(CoordRec_list)
#print 'matrix l is = %s'%(l)
A = matrix_A(CoordRec_list)
print 'matrix A is = %s'%(A)
#P = optimal_line(CoordRec_list)
#print 'matrix P is = %s'%(P)






