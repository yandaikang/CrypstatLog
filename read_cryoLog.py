import numpy as np
import h5py
from scipy import signal
import struct;
import sys, os
import glob
import scipy.optimize as opt
import matplotlib.pyplot as plt
import matplotlib as mpl
from scipy.optimize import curve_fit
from shutil import copyfile
import time as Time
import matplotlib.dates as mdates
import datetime
mpl.rc('figure', facecolor = 'w')


#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#read in noise data
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
filelist = glob.glob('Regul*.txt')

for filename in filelist:
	#filename = 'Regul-03_08_2017-16_52_09.txt'

	datafile = open(filename, 'r')
	data=[]
	for line in datafile:
		data.append(line)
	datafile.close()

	time=[]
	temp=[]
	for i in range(1, len(data)):
		daystamp = data[i].split(',')[0].split()[0].split('/')
		timestamp = data[i].split(',')[0].split()[1].split(':')

		#abstime = float(data[i].split(',')[1])
		abstime = datetime.datetime(int(daystamp[2]), int(daystamp[0]), int(daystamp[1]), int(timestamp[0]), int(timestamp[1]), int(timestamp[2].split('.')[0]))
		time.append(abstime)
		
		temp50mK = float(data[i].split(',')[10])
		temp.append(temp50mK)

	time=np.array(time)
	#time -= time[0]

	temp = np.array(temp)*1000

	plt.plot(time, temp, label=filename)


plt.xlabel('Time [s]')
plt.ylabel('Temperature [mK]')

plt.xticks(rotation=45)

plt.legend(loc='upper right')
plt.tight_layout()
plt.show()

