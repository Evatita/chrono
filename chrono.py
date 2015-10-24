#! /usr/bin/python

import sys
import datetime

'''
def read_cts_file(self):
    
  with open(ct, 'r') as buf:
    line = buf.readline()
    
    while line:
      if line[0] == "#":
        pass
      elif line[1] == "+"          
        pass
      else:
        print line
      line = buf.readline()

class CoordRec():

  CoordRec_list =[]

  def __init__(self, x, y, z):
   self.__x = final_x
   self.__y = final_y
   self.__z = final_z
'''
class CoordRec:

  CoordRec_list = []

  def __init__(self, ctsfile):

    with open(ctsfile, 'r') as buf:
      line = buf.readline()
      
      while line:
        if line[0] == '#':
          pass
        elif line[1] == '+':
          pass
        else:
          print line
        line = buf.readline

ctsfile(sys.argv[1])
#ctsfile = sys.argv[1]
#read_cts_file(sys.argv[1])
