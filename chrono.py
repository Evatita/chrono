#! /usr/bin/python

import sys
import datetime

CoordRec_list = []

def read_cts_file(ct):

    with open(ct, 'r') as buf:
        line = buf.readline()
        
        while line:
            if line[0] == "#":
                pass
            #elif line[1] == "+":          
            #    pass
            else:
                try:
                    cr = CoordRec(line)
                    CoordRec_list.append(cr)
                except:
                    print 'Invalid line: [%s]; line skipped'%(line)
            line = buf.readline()

def compute_average_x(cr_list):
    sum_of_x = 0
    for i in cr_list:
        sum_of_x = sum_of_x + i.x()
    return sum_of_x / len(cr_list)

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
     
#ctsfile = sys.argv[1]
read_cts_file(sys.argv[1])
print 'I have read %i elements'%(len(CoordRec_list))
x_mean = compute_average_x(CoordRec_list)
print 'Average value of x = %10.3f'%(x_mean)
