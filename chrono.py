#! /usr/bin/python

import sys

def read_cts_file(ct):

  with open(ct, 'r') as buf: 
    line = buf.readline()

    while line:
      if line[0] == "#":
        pass
      else:
        print line
      line = buf.readline()

#   for line in buf:
#      columns = line.split()
#      if len(columns) <= 11:
#        print columns[10]

# ctsfile = sys.argv[1]
read_cts_file(sys.argv[1])
