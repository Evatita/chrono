#! /usr/bin/python

import sys, os, re
import datetime
import numpy as np
import matplotlib.pyplot as pl
import matplotlib.dates as mdates

PATH2PLT = '/home/eva/Software/bern52/GPSDATA/CAMPAIGN52/EPNDENS1/OUT'
PLTFILE  = 'gr_2013.PLT'

def read_plt(fn):
  with open(fn, 'r') as buf:
    epochs_array = []
    rest_array   = []
    for line in buf.readlines():
      l = line.split()
      assert len(l) == 5
      dt_str = float(l[5])
      station = l[1]
      epochs_array.append(dr_str)
      rest_array.append(x for x in l[4])
      
  ##  sort the elements of the two lists based in date (i.e. epochs_array)
  ##  this will create a new list with len()=2, where the first list is the
  ##+ sorted epochs_array and the second is the corresponding rest_array
      sorted_lst = [list(x) for x in zip(*sorted(zip(epochs_array, rest_array), key=lambda pair: pair[0]))]
  ##  Now, sorted_lst[1] contains lists of type: [x,y,z,sx,sy,sz]. Transpose that
  ##  so that we can easily read np.array(s) (i.e. make sorted_lst[1]=[[x1,x2,...],[y1,y2,...]...]]
      rest_array = map(list, zip(*sorted_lst[1]))

  ## Return a TimeSeries object
      return pl.TimeSeries(name=read_plt, type=float,
                    epoch_array = sorted_lst[0], ## the epochs list (NOT ARRAY)
                    sn_array     = np.array(rest_array[0]),
                    se_array     = np.array(rest_array[1]),
                    su_array     = np.array(rest_array[2]))

def plot_plt(read_plt, y_erbar=False):
  mdates_series = mdates.date2num(epoch_array)
  min_mdt       = mdates.date2num(epoch_array - datetime.timedelta( days = 1.0))
  max_mdt       = mdates.date2num(epoch_array - datetime.timedelta( days = 1.0))
  
  fig, axs = plt.subplots(3, sharex = True)
  axs[0].plotdate(min_mdt, max_mdt)
  
  if not y_erbar:
    axs[0].plotdate(x=mdates_series, y=sn_array, fmt='-')
  else:
    axs[0].errorbar(x=mdates_series, y=sn_array, xerr=None, fmt='-', yerr=sn_array, ecolor='0.1')
    axs[0].set_title('Station %s'%station)
    axs[0].set_ylabel('Dnorth (m)')
    
    axs[0].xaxis.set_major_locator(mdates.YearLocator())
    axs[0].xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
    axs[0].xaxis.set_minor_locator(mdates.MonthLocator(bymonth=[1,3,6,9,12]))
    
    fig.autofmt_xdate()
    pl.savefig('%s.eps'%station)
    pl.show()
    
read_plt = os.path.basename(sys.argv[1])

sys.exit(0)