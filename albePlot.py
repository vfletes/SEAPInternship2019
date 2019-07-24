#! /bin/usr/python2
import matplotlib.pyplot as plt
import numpy as np
import csv
import os

from IPython import embed as shell

x = []
y = []

RI_data = open('/calval_npp2/fletes/dataFiles/AL_SHIPS_1982_2017_TC_RI.txt','r')
RI_name_data = open('/calval_npp2/fletes/dataFiles/AL_SHIPS_1982_2017_TC_RI_name.txt','r')
head_line = RI_name_data.readline() #getting first line of RITC names list, only need to change this line for storm change!! <-- very important
splitted = head_line.split() #splitting the first line of RITC names list
marker = str(splitted[0] + ' ' + splitted[1] + ' ' + splitted[2]) #getting the date and time of the RI of the TC
storm = splitted[0] #getting the name of the TC
date = splitted[1]#beginning storm date
stormYr = date[:2]#year of storm
counter = 0

for row in RI_data:
        line = row.split()
        if line[-1] == 'HEAD' and line[0] == storm and stormYr in line[1]:
                x.append(counter)
                y.append(int(line[3]))
                if marker in row:
                        x1 = counter
                        y1 = int(line[3]) + 5
                counter += 6

plt.plot(x,y)
plt.xlabel('Hours Since Storm Data Began')
plt.ylabel('Wind Speeds')
plt.title(storm + ' Storm Data')
plt.errorbar(x1, y1, yerr=5, label='Rapid Intensification Starts') #yerr = line height, xerr = line width
plt.legend()
plt.show()
