#! /usr/bin/python

##  station
##  start doy
##  stop doy

import sys, os, re
import datetime
import bernutils.geodesy
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

PATH2CRD = '/home/bpe/data/GPSDATA/CAMPAIGN52/LEFK15/STA'
CRDFILE  = 'DSOYYDDD0.CRD'
YEAR     = 2015

def generate_crd_file( year, doy ):
    if year > 2000 : yr2 = int( year - 2000 )
    else:            yr2 = int( year - 1900 )
    return os.path.join(PATH2CRD, 
            CRDFILE.replace('YY', '%02i'%(yr2)).replace('DDD', '%03i'%(doy))
            )

def get_xyz( station, crdfile ):
    with open( crdfile, 'r' ) as f:
        for line in f.readlines():
            if re.search(' %s '%(station), line):
                l = line[20:67].split()
                try:
                    x, y, z = map(float, l)
                    return x, y, z
                except:
                    raise RuntimeError('Failed to resolve crd in file ' + crdfile)
        print '[WARNING] Station \"%s\" not matched in file \"%s\"'%( station, crdfile )
        return None

def xyz_mean( xyz_list ):
    xm = .0
    ym = .0
    zm = .0
    pts = float( len( xyz_list ) )
    for i in xyz_list:
        xm += i[0]; ym += i[1]; zm += i[2]
    return xm/pts, ym/pts, zm/pts

def ydoy2pdt( year, doy ):
    return datetime.datetime.strptime('%4i %03i 12 00 00'%(year, doy), '%Y %j %H %M %S')

def subseries( list_of_tuples, comp ):
    return [ x[comp] for x in list_of_tuples ]

station   = sys.argv[1]
start_doy = int( sys.argv[2] )
stop_doy  = int( sys.argv[3] )

if start_doy > stop_doy :
    print >> sys.stderr, 'Invalid start/end doy'
    sys.exit( 1 )

xyz_series = []
neu_series = []
pdt_series = []

for doy in range(start_doy, stop_doy + 1):
    crdfile = generate_crd_file( YEAR, doy )
    t_xyz = get_xyz( station, crdfile )
    if t_xyz is not None:
        xyz_series.append( t_xyz )
        pdt_series.append( ydoy2pdt( YEAR, doy ) )

average_xyz = xyz_mean( xyz_series )

with open('%s.neu'%(station), 'w') as fout:
    idx = 0
    for xyz in xyz_series:
        neu = bernutils.geodesy.cartesian2topocentric(
                        average_xyz[0], average_xyz[1], average_xyz[2],
                        xyz[0], xyz[1], xyz[2])
        neu_series.append( neu )
        print>>fout, '%s %+08.4f %+08.4f %+08.4f'%(
                pdt_series[idx].strftime('%Y-%m-%d'), neu[0], neu[1], neu[2]
                )
        idx += 1
print 'NEU components saved as \"%s.neu\"'%(station)


mdates_series = mdates.date2num( pdt_series )
min_mdt = mdates.date2num( min( pdt_series ) - datetime.timedelta( days=0.5 ) )
max_mdt = mdates.date2num( max( pdt_series ) + datetime.timedelta( days=0.5 ) )

fig, axs = plt.subplots(3, sharex=True )
axs[0].set_xlim( min_mdt, max_mdt )

axs[0].plot_date( x=mdates_series, y=subseries(neu_series, 0), fmt="ro" )
axs[0].set_title( 'Station %s'%station )
axs[0].set_ylabel( 'DNorth (m)' )

axs[1].plot_date( x=mdates_series, y=subseries(neu_series, 1), fmt="ro" )
axs[1].set_ylabel( 'DEast (m)' )

axs[2].plot_date( x=mdates_series, y=subseries(neu_series, 2), fmt="ro" )
axs[2].set_ylabel( 'DUp (m)' )

axs[0].xaxis.set_major_locator( mdates.DayLocator() )
axs[0].xaxis.set_major_formatter( mdates.DateFormatter('%d/%b') )
axs[0].format_xdata = mdates.DateFormatter( '%m-%dT%H' )

fig.autofmt_xdate()

plt.savefig( '%s.png'%station, bbox_inches='tight' )
plt.savefig( '%s.eps'%station )

print 'Plots saved as \"%s.png\" and \"%s.eps\"'%(station, station)

sys.exit( 0 )
