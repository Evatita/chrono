#! /usr/bin/python

import os, sys, re
import datetime as dt
import numpy as np
import matplotlib.pyplot as plt

## EVL file contains the events from FODITS analysis, i.e. periodic functions, velocities changes,
## discontinuties and decteted outliers, with the following format:
## Station(0) Flg Event(1), From Epoch(2), To Epoch(3), Period(4), sN[m](5), sE[m](6), sU[m](7), S, Remark
## Periodic funtions are remarked as EST PERI, velocities changes as EST RATE, discontinuties as 
## EST DISC and detected outliers as EST OUTL.

def read_evl(evl_file):
  
  with open(evl_file, 'r') as buf:
    events  = []
    epochs  = []
    sN      = []
    SE      = []
    sU      = []
    
    line = buf.readline()
    for line in buf.readline():
      while re.search(' %s ' %(station), line):
        l = line[0:116].split()
        if re.search(' %s ' %('EST PERI'), line):
          station       = l[0]
          evl_peri      = l[1]
          period        = l[15]
          residualn     = l[16]
          residuale     = l[17]
          residualu     = l[18]
          l = buf.readline().split()
        elif re.search(' %s ' %('EST RATE'), line):
          station       = l[0]
          evl_rate      = l[1]
          epoch_rate    = l[3] + '-' + l[4] + '-' + l[5] + ':' + int(l[6])*3600 + int(l[7])*60 + int(l[8])
          residualn     = l[16]
          residuale     = l[17]
          residualu     = l[18]
          l = buf.readline().split()
        elif re.search(' %s ' %('EST DISC'), line) :
          station       = l[0]
          evl_disc      = l[1]
          epoch_disc    = l[3] + '-' + l[4] + '-' + l[5] + ':' + int(l[6])*3600 + int(l[7])*60 + int(l[8])
          residualn     = l[16]
          residuale     = l[17]
          residualu     = l[18]
          l = buf.readline().split()
        elif re.search(' %s ' %('EST OUT'), line):
          station       = l[0]
          evl_out       = l[1]
          epoch_start   = l[3] + '-' + l[4] + '-' + l[5] + ':' + int(l[6])*3600 + int(l[7])*60 + int(l[8])
          epoch_end     = l[9] + '-' + l[10] + '-' + l[11] + ':' + int(l[12])*3600 + int(l[13])*60 + int(l[14])
          residualn     = l[16]
          residuale     = l[17]
          residualu     = l[18]
          return
        if evl_peri == evl_rate or evl_peri == evl_disc:
          raise RuntimeError("Invalid EVL format (events)")
        events.append(evl_peri, evl_rate, evl_disc, evl_out)
        epochs.append(epoch_rate, epoch_disc, epoch_start, epoch_end)
        sN.append(residualn)
        sE.append(residuale)
        sU.append(residualu)
        line = buf.readline()
 '''       
def evl_plot(read_evl, y_erbar= False):
  min_dt = dt.date(2000, 01, 01)
  max_dt = dt.date(2016, 01, 01)
  
  fig, axs = plt.subplots(3, sharex=True )
  axs[0].set_xlim( min_dt, max_dt )
  
  if not y_erbar:
    axs[0].plotdate(dates, opens ,fmt='-')
  else:
    axs[0].errorbar(dates)
  '''  
evl_file = sys.argv[1]
station  = sys.argv[2]

sys.exit(0)