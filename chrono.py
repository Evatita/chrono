#! /usr/bin/python

import sys
import datetime

def read_cts_file(ct):

  with open(ct, 'r') as buf:
    line = buf.readline()
    
    while line:
      if line[0] == "#":
        pass
      elif line[1] == "+":          
        pass
      else:
        print line
      line = buf.readline()

class CoordRec:
  CoordRec_list = []

  def __init__(self, line)
    global line
      l = line.split()
      self.x = l[6]
      self.y = l[7]
      self.z = l[8]
     




#ctsfile = sys.argv[1]
read_cts_file(sys.argv[1])
