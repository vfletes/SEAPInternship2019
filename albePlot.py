#! /bin/usr/python2
import matplotlib.pyplot as plt
import numpy as np
import csv
import os
import math
#ctrl-r redoes an action
from IPython import embed as shell
import datetime as dt
plt.rcParams.update({'xtick.labelsize': 6})
def setXY(fileName, stormIndex):
        x = []
        y = []
        xLabels = []
        RI_name_data = open(fileName[:-4] +'_name' + fileName[-4:],'r') #name file
        for n in range(stormIndex):
                head_line = RI_name_data.readline()
        splitted = head_line.split() #splitting the first line of RITC names list
        marker = str(splitted[0] + ' ' + splitted[1] + ' ' + splitted[2]) #getting the date and time of the RI of the TC
        storm = splitted[0] #getting the name of the TC
        date = splitted[1]#beginning storm date
        stormYr = date[:2]#year of storm
        with open(fileName,'r') as RI_data:
                row = RI_data.readline()
                while row:
                        line = row.split()
                        sYU = line[1]
                        stormYearU = str(sYU[:2])
                        if line[-1] == 'HEAD' and line[0] == storm and stormYr == stormYearU:
                                xVar = str(line[1]) + str(line[2])
                                xLabels.append(xVar)
                                date = dt.datetime.strptime(xVar,'%y%m%d%H')
                                xVar = float(xVar)
                                #xVal = math.floor(uxVar/100.)*100. + ((uxVar/100.)%1.0)*25./.06 #uxVar was the date+hour-yearFromBeginning
                                xVal = int(date.strftime('%s'))
                                x.append(xVal)
                                line2 = RI_data.readline().split()
                                y.append(int(line2[2]))
                                if marker in row:
                                        x1 = xVal
                                        y1 = int(line2[2]) + 5
                        row = RI_data.readline()
        plt.plot(x,y)
        plt.xticks(x, xLabels)
        plt.xlabel('Year, Month, Day, and Time of Storm')
        plt.ylabel('Wind Speeds')
        plt.title(storm + ' Storm Data')
        plt.errorbar(x1, y1, yerr=5, label='Rapid Intensification Starts') #yerr = line height, xerr = line width
        plt.legend()
setXY('/calval_npp2/fletes/dataFiles/AL_SHIPS_1982_2017_TC_RI.txt', 15)
plt.show()
