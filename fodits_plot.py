#! /usr/bin/python

import sys, os
import datetime
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

#Need to change PLTFILE when needed!!

PATH2CRD = '/home/eva/Software/bern52/GPSDATA/CAMPAIGN52/EPNDENS1/OUT/'
PLTFILE  = 'gr_2013.PLT'

def readplt(fn):
  line_dict = {}
    
  with open(fn, 'r') as buf:
    line = buf.readline()
        
    while line and line[47:].strip():
      key = line[47:].rstrip()
      val = line[0:47].strip()
      if key == '1'[22:23]:
        line_dict['Station'] = line[0:4]
        line_dict['sN']      = float(line[27:37].rstrip())
        line_dict['doy']     = float(line[37:47].rstrip())
      elif key == '2'[22:23]:
        line_dict['Station'] = line[0:4]
        line_dict['sE']      = float(line[27:37].rstrip())
        line_dict['doy']     = float(line[37:47].rstrip())
      elif key == '3'[22:23]:
        line_dict['Station'] = line[0:4]
        line_dict['sU']      = float(line[27:37].rstrip())
        line_dict['doy']     = float(line[37:47].rstrip())
      else:
        line_dict[key] = val
      line = buf.readline()

  return line_dict

pltfile    = os.path.basename(sys.argv[1])
dictionary = readplt(sys.argv[1])

try:
  print "station name: %s" %dictionary['Station']
     #%(dictionary['Station'], dictionary['sN'], dictionary['sE'], dictionary['sU'])   
except:
  print 'ERROR !!! Fodits_plt file: ', plt_file
  
sys.exit(0)