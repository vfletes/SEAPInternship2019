#! /bin/usr/python2

import matplotlib.pyplot as plt
import numpy as np
import csv
import os
#need to finish: make the graph continue to go left instead of cycling
from IPython import embed as shell

x = []
y = []

RI_data = open('/calval_npp2/fletes/code/AL_SHIPS_1982_2017_TC_RI.txt','r')
RI_name_data = open('/calval_npp2/fletes/code/AL_SHIPS_1982_2017_TC_RI_name.txt','r')
head_line = RI_name_data.readline() #getting first line of RITC names list
splitted = head_line.split() #splitting the first ling
marker = str(splitted[0] + ' ' + splitted[1] + ' ' + splitted[2]) #getting the date and time of the RI of the TC
storm = splitted[0] #getting the name of the TC
counter = 0 #change, but works for now
for row in RI_data:
        line = row.split()
        if line[-1] == 'HEAD' and line[0] == 'ALBE' and '82' in line[1]:
                x.append(counter)
                y.append(int(line[3]))
                counter += 6
                if marker in row:
                        x1 = counter
                        y1 = int(line[3])
plt.plot(x,y)
plt.xlabel('Hours Since Rapid Intensification Started')
plt.ylabel('Wind Speeds')
#yee = np.linspace(0.05, 0.2, 10)
#plt.errorbar(x1, y1, yerr=yee)
#an error is occuring above bc i don't understand how errorbars, linspace, and yerr works
plt.title('ALBE Storm Data')
plt.legend()
plt.show()
