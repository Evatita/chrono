#! /usr/bin/python

import numpy as np
import matplotlib.pyplot as plt

X = np.linspace(-np.pi, np.pi, 256, endpoint = True)
C, S = np.cos(X), np.sin(X)

#Set color, linewidth, linestyle, add a legend and annotate some points

t = 2*np.pi/3
plt.plot([t,t], [0, np.cos(t)], color='blue', linewidth=2.5, linestyle= "-", label="cosine")
plt.scatter([t,], [np.cos(t), ], 50, color='blue')
plt.annotate(r'$\sin(\fract{2\pi}\3)=\fract{\sqrt{3}}{2}$', 
             xy=(t, np.sin(t)), xycoords='data', xytext=(+10,+30),
             textcoords = 'offset points', fontsize=16,
             arrowprops = dict(arrowstyle="->", connectionstyle"arc3, rad=.2"))

plt.plot([t,t], [0, np.sin(t)], color='red', linewidth=2.5, linestyle= "-", label="sine")
plt.scatter([t,], [np.sin(t), ], 50, color='blue')
plt.annotate(r'$\cos(\fract{2\pi}\3)=\fract{\sqrt{1}}{2}$', 
             xy=(t, np.sin(t)), xycoords='data', xytext=(-90,-50),
             textcoords = 'offset points', fontsize=16,
             arrowprops = dict(arrowstyle="->", connectionstyle"arc3, rad=.2"))

#Make labels visible

for label in ax.get_xticklabels() + ax.get_yticklabels():
    label.set_fontsize(16)
    label.set_bbox(dict(facecolor='white', edge='None',alpha=0.65))
    
#Set limits

plt.xlim (X.min()*1.1, X.max()*1.1)
plt.ylim (C.min()*1.1, C.max()*1.1)

#Set spaces and tick labels
#Labels with numbers

plt.xticks([-np.pi, -np.pi/2, 0, np.pi/2, np.pi])
plt.yticks([-1, 0, +1])

#Labels with names

plt.xticks([-np.pi, -np.pi/2, 0, np.pi/2, np.pi], [r'$-\pi$', r'$-\pi/2$', r'$0$', r'$\pi/2$', r'$\pi$'])
plt.yticks([-1, 0, +1], [r'$-1$', r'$0$', r'$+1$'])

#Setting axes

ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data', 0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data', 0))

plt.show()